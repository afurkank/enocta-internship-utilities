# How to use

```
from extract_info import get_info

input = "Zaman yönetimiyle ilgili, en fazla 1 saatlik ve ileri seviye eğitimlere ihtiyacım var."

output_dict = get_info(
    input=input,
    path="path to your .env file",
    model="gpt-4",
    temperature=0.0
)

print(output_dict["need"])
print(output_dict["min_time"])
print(output_dict["max_time"])
print(output_dict["level"])
```

Do not forget to do

`pip install -r requirements.txt`

to install the necessary packages and libraries.
