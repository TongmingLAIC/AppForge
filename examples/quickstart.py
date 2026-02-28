import argparse
import json
from pathlib import Path

from AppForge import AppForge


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quickstart runner for AppForge (naive baseline)")
    parser.add_argument("--task_id", type=int, default=63, help="Task id to run (default: 63)")
    parser.add_argument("--run_name", default="quickstart_naive", help="Run folder name")
    parser.add_argument("--base_folder", default="runs", help="Output base folder")

    parser.add_argument("--use_docker", action="store_true", help="Use docker runtime")
    parser.add_argument("--docker_name", default="zenithfocuslight/appforge:latest", help="Docker image name")
    parser.add_argument("--docker_port", type=int, default=6080, help="Docker port")

    parser.add_argument("--emulator_id", default="emulator-5554", help="ADB device id for local mode")
    parser.add_argument("--bench_folder", default=None, help="Path to AppForge_Bench for local mode")
    parser.add_argument("--sdk_path", default=None, help="Android SDK path for local mode")
    return parser.parse_args()


def run_quickstart(args: argparse.Namespace) -> dict:
    base_folder = Path(args.base_folder).resolve()
    base_folder.mkdir(parents=True, exist_ok=True)

    if args.use_docker:
        evaluator = AppForge(
            runs=args.run_name,
            base_folder=base_folder,
            use_docker=True,
            docker_name=args.docker_name,
            docker_port=args.docker_port,
        )
    else:
        if not args.bench_folder or not args.sdk_path:
            raise ValueError("Local mode requires --bench_folder and --sdk_path")
        evaluator = AppForge(
            runs=args.run_name,
            base_folder=base_folder,
            emulator_id=args.emulator_id,
            bench_folder=Path(args.bench_folder).resolve(),
            sdk_path=Path(args.sdk_path).resolve(),
        )

    try:
        task_id = args.task_id
        template_strings = evaluator.template_folder / "empty_activity/app/src/main/res/values/strings.xml"
        changed = {"app/src/main/res/values/strings.xml": template_strings.read_text(encoding="utf-8")}

        compile_error = evaluator.compile_json_based_on_template(changed, task_id, raw_log="quickstart-naive")
        if compile_error:
            print("Compile errors:")
            print(compile_error)

        result = evaluator.evaluation_only_test([task_id])
        return result
    finally:
        evaluator.clean_up()


if __name__ == "__main__":
    output = run_quickstart(parse_args())
    print(json.dumps(output, indent=2, ensure_ascii=False))
