from extract_info import get_info

input = "Mehmet Auf'tan strese dair 1 ile 2 saat arasında başlangıç seviyesinde eğitimler almak istiyorum. Yardımcı olabilir misin?"

output_dict = get_info(
    input=input,
    path="path to your .env file",
    model="gpt-4",
    temperature=0.0
)

print(output_dict["need"])
print(output_dict["teacher"])
print(output_dict["min_time"])
print(output_dict["max_time"])
print(output_dict["level"])
