import json
from extract_info import get_info
import time

path_to_env = "path to your .env file"

file_path = r"data.json"
with open(file_path, "r") as file:
    data = json.load(file)

input = "Kodlama ile ilgili 8 saatlik ileri seviye eğitime ihtiyacım var. Yardımcı olabilir misin?"

model = 'gpt-4'
temperature = 0.0

start_time = time.time()

output_dict = get_info(
    input=input,
    path=path_to_env,
    model=model,
    temperature=temperature
)

end_time = time.time()

time_taken = end_time - start_time

min_time = output_dict["min_time"]
min_time = int(min_time) if min_time != '-' else '-'

max_time = output_dict["max_time"]
max_time = int(max_time) if max_time != '-' else '-'

level = output_dict["level"]
level = level.capitalize() if level != '-' else '-'

log_dict = {
    "need":output_dict["need"],
    "instructor":output_dict["teacher"],
    "min time":min_time,
    "max time":max_time,
    "level":output_dict["level"].capitalize()
}

param_dict = {
    "model":model,
    "temperature":temperature
}

log = {"input" : input, "parameters" : param_dict, "output" : log_dict, "completion time" : round(time_taken, 2)}

data.append(log)

model = 'gpt-3.5-turbo'
temperature = 0.0

start_time = time.time()

output_dict = get_info(
    input=input,
    path=path_to_env,
    model=model,
    temperature=temperature
)

end_time = time.time()

time_taken = end_time - start_time

min_time = output_dict["min_time"]
min_time = int(min_time) if min_time != '-' else '-'

max_time = output_dict["max_time"]
max_time = int(max_time) if max_time != '-' else '-'

level = output_dict["level"]
level = level.capitalize() if level != '-' else '-'

log_dict = {
    "need":output_dict["need"],
    "instructor":output_dict["teacher"],
    "min time":min_time,
    "max time":max_time,
    "level":output_dict["level"].capitalize()
}

param_dict = {
    "model":model,
    "temperature":temperature
}

log = {"input" : input, "parameters" : param_dict, "output" : log_dict, "completion time" : round(time_taken, 2)}

data.append(log)

with open(file_path, "w") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
