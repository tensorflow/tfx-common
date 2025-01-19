# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script to use beam.run_inference from command line
Below is a complete command in terminal for running this script
on dataflow for benchmarks.

python3 run_inference_benchemark.py \
PATH_TO_MODEL \
PATH_TO_DATA \
--output gs://YOUR_BUCKET/results/output \
--extra_packages PACKAGE1 PACKAGE2 \
--project YOUR_PROJECT \
--runner DataflowRunner \
--temp_location gs://YOUR_BUCKET/temp \
--job_name run-inference-metrics \
--region us-central1

*In this case, one of the extra_packages should be the wheel file for tfx-bsl
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import apache_beam as beam
from tfx_bsl.tfxio import raw_tf_record
from tfx_bsl.beam import run_inference
from tfx_bsl.public.proto import model_spec_pb2
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions


def run(argv=None, save_main_session=True):
    """Main entry point; defines and runs the user_score pipeline."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'model_path',
        type=str,
        help='The path to input model')
    parser.add_argument(
        'input',
        type=str,
        help='Path to the data file(s) containing data.')
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='Path to the output file(s).')
    parser.add_argument(
        '--extra_packages',
        type=str,
        nargs='*',
        help='Wheel file(s) for any additional required package(s) to Beam packages')

    args, pipeline_args = parser.parse_known_args(argv)
    options = PipelineOptions(pipeline_args)

    setup_options = options.view_as(SetupOptions)
    setup_options.extra_packages = args.extra_packages
    setup_options.save_main_session = save_main_session

    def get_saved_model_spec(model_path):
        '''Returns an InferenceSpecType object for a saved model path'''
        return model_spec_pb2.InferenceSpecType(
            saved_model_spec=model_spec_pb2.SavedModelSpec(
                model_path=model_path))

    inference_spec_type = get_saved_model_spec(args.model_path)
    converter = raw_tf_record.RawTfRecordTFXIO(
        args.input, raw_record_column_name='__RAW_RECORD__')

    with beam.Pipeline(options=options) as p:
        (p
            | "GetRawRecordAndConvertToRecordBatch" >> converter.BeamSource()
            | 'RunInferenceImpl' >> run_inference.RunInferenceImpl(
                inference_spec_type))


if __name__ == '__main__':
    run()
