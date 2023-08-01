from get_answer import get_answer

from chainlit import AskUserMessage, Message, on_chat_start

@on_chat_start
async def main():
    opening_prompt = """Merhaba, ben Enocta'nın sohbet servisiyim. Size ihtiyacınız olan
    eğitimleri önermekle görevliyim. Hangi konuda eğitime ihtiyacınız olduğunu öğrenebilir miyim?"""

    time_prompt = """Sana daha doğru eğitimler önerebilmem için eğer istersen bu eğitimlerin bulunması 
    gerektiği süre aralığını belirtebilirsin."""

    level_prompt = """Son olarak eğitimlerin hangi seviyede olması gerektiğini belirtebilirsin. 
    Başlangıç, orta ve ileri seviyede eğitimlerimiz var."""
    
    customer_need_response = None
    customer_time_response = None
    customer_level_response = None

    need_res = await AskUserMessage(
        content=opening_prompt,
        author="Enocta",
        timeout=100
    ).send()
    if need_res:
        customer_need_response = need_res['content']
        time_res = await AskUserMessage(
            content=time_prompt,
            author="Enocta",
            timeout=100
        ).send()
        if time_res:
            customer_time_response = time_res['content']
            level_res = await AskUserMessage(
                content=level_prompt,
                author="Enocta",
                timeout=100
            ).send()
            if level_res:
                await Message(content="Senin için uygun eğitimleri arıyoruz...", author="Enocta",).send()
                customer_level_response = level_res['content']
                answer = get_answer(
                    customer_need_response,
                    customer_time_response,
                    customer_level_response
                )
                await Message(content=answer, author="Enocta",).send()