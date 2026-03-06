#### 🚀 Local Emulator Setup

##### Prerequisite

Make sure you have Android Studio and SDK installed on your machine. For users who haven't installed these prerequisites, you can check https://github.com/TongmingLAIC/AppForge/blob/main/documentation/local_emulator.md. However, if you don't have them installed on your machine before and are able to use Ubuntu system with CPU virtualization, we strongly recommend you to use docker environment. 

##### Download Evaluation Files

Download evaluation repo and install dependencies.

```bash
git clone https://github.com/TongmingLAIC/AppForge_Bench
cd AppForge_Bench

conda create -n appforge python=3.10
conda activate appforge
pip install -r requirements.txt

python -m uiautomator2 init
```

### 🚀 Environment Setup
Then download then repo and install our module **AppForge**:

```bash
git clone https://github.com/TongmingLAIC/AppForge

cd AppForge
pip install -e .
# or to run our examples (recommended):
pip install -e .[example]
```



#### 🔰 Quick Start with Local Emulator
Keep the emulator open, we can run following code with **local emulator**s:

```
python examples/test.py --emulator_id <emulator_id> --bench_folder <position_where_you_pull_the_AppBench_forge> --sdk_path <sdk_path> \
--model=qwen3coder --runs=example_qwen3 --api_key_path=<api_key_path> --start_id 63 --end_id 63 --self_fix_attempts 1
```

For example on our machine we run following command:

```
python examples/test.py --emulator_id  emulator-5554 --bench_folder /mnt/AppForge-Bench --sdk_path /home/Android/sdk \
--model=qwen3coder --runs=example_qwen3 --api_key_path=dash_scope.key --start_id 63 --end_id 63 --self_fix_attempts 1
```

#### 🔰 Other Configurations
To activate self-fix with more or less compilation feedback, set parameter value *--self_fix_attempts*. 

To record videos when testing, set parameter option *--record_video*.

The tasks are in https://github.com/TongmingLAIC/AppForge/blob/main/tasks/tasks.json (0-indexed).

More information can be seen in the source code and the document https://appforge-bench.github.io/code-docs/modules.html.

