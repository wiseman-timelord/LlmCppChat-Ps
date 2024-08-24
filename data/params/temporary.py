# .\data\params\temporary.py

# Imported Modules
import argparse
import os
import platform

# General Variables
last_session_history = None
rotation_counter = 0
selected = None

# Model Variables
loaded_models = {}
llm = None

# Sound Variables
last_sound_event = None
TTS_RATE = 150  
TTS_VOLUME = 0.9  
TTS_VOICE_ID = 1
tts_counter = 0

# File Paths
YAML_PATH = './data/params/persistent.yaml'
LLAMA_CLI_PATH = r".\libraries\llama-b3617-bin-win-vulkan-x64\llama-cli.exe"
SOUND_DIRECTORY = "./data/sounds"

# Tasks
VALID_TASKS = ['converse', 'consolidate', 'emotions']

# Model Mapping
agent_TYPE_TO_TEMPERATURE = {
    'chat': 0.5,
    'instruct': 0.25
}

PROMPT_TO_MAXTOKENS = {
    'converse': 100,
    'consolidate': 200,
    'emotions': 300
}

CONTEXT_LENGTH_MAP = {
    'chat': {
        '4k': 4096,
        '8k': 8192,
        '16k': 16384
    }
}

# Keys to be managed in YAML
ORDERED_KEYS = [
    'human_name', 'agent_name', 'agent_role', 
    'scenario_location', 'agent_emotion', 'session_history',
    'human_input', 'agent_output_1', 'agent_output_2', 
    'agent_output_3', 'sound_event', 'context_length',
    'syntax_type', 'model_path'
]
KEYS_TO_CLEAR = [
    'human_name', 'agent_name', 'agent_role', 
    'scenario_location', 'agent_emotion', 'session_history',
    'human_input', 'agent_output_1', 'agent_output_2', 
    'agent_output_3', 'sound_event', 'context_length_1',
    'context_length_2', 'syntax_type_1', 'syntax_type_2',
    'model_path_1', 'model_path_2' 
]

# Syntax Options
SYNTAX_OPTIONS_DISPLAY = [
    "{combined_input}",
    "User: {combined_input}",
    "User:\\n{combined_input}",
    "### Human: {combined_input}",
    "### Human:\\n{combined_input}",
    "### Instruction: {combined_input}",
    "### Instruction:\\n{combined_input}",
    "{system_input}. USER: {instruct_input}",
    "{system_input}\\nUser: {instruct_input}"
]
SYNTAX_OPTIONS = [
    "{combined_input}",
    "User: {combined_input}",
    "User:\n{combined_input}",
    "### Human: {combined_input}",
    "### Human:\n{combined_input}",
    "### Instruction: {combined_input}",
    "### Instruction:\n{combined_input}",
    "{system_input}. USER: {instruct_input}",
    "{system_input}\nUser: {instruct_input}"
]

# Parser Variables
parser = argparse.ArgumentParser(description='Global argument parser for all scripts.')
parser.add_argument('--logs', action='store_true', help='Enable writing of raw output to logs')
parser.add_argument('--tts', action='store_true', help='Enable text-to-speech')
parser.add_argument('--sound', action='store_true', help='Enable sounds')
args = parser.parse_args()

# System Information
os_name = platform.system()
if os_name == 'Windows':
    WINDOW_TITLE_1 = 'Chat-VulkanLlama-Window1'
    WINDOW_TITLE_2 = 'Chat-VulkanLlama-Window2'
    WINDOW_SIZE = "echo -e \e[8;45;90t"
else:
    WINDOW_TITLE_1 = '\x1b]2;Chat-VulkanLlama-Window1\x07'
    WINDOW_TITLE_2 = '\x1b]2;Chat-VulkanLlama-Window2\x07'
    WINDOW_SIZE = "mode con: cols=90 lines=45"