from langgraph.graph import StateGraph, START, END
from typing import List
from pydantic import BaseModel, Field
from langchain_mistralai import ChatMistralAI
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import asyncio
load_dotenv()

class State(BaseModel):
    limit: int
    nums: List[int] = Field(default_factory=list)
    type: List[str] = Field(default_factory=list)

rate_limiter = InMemoryRateLimiter(
    requests_per_second=1.0,
    check_every_n_seconds=0.1,
    max_bucket_size=1
)

prompt = PromptTemplate(
    template='''Is {number} odd or even. Just say "odd" or "even"''',
    input_variables=['number']
)

llm = ChatMistralAI(
        model="ministral-8b-latest",
        rate_limiter=rate_limiter
    )

async def identify(state: State) -> State:
    chain = prompt | llm
    tasks = [
        chain.ainvoke({'number': i})
        for i in range(1, state.limit)
    ]
    results = await asyncio.gather(*tasks)
    return {
        "nums": list(range(1, state.limit)),
        "type": [r.content.strip().lower() for r in results]
    }


async def main():
    graph = StateGraph(State)
    graph.add_node("identify", identify)
    graph.add_edge(START, "identify")
    graph.add_edge("identify", END)
    graph = graph.compile()
    res = await graph.ainvoke({'limit': 10})
    print(res['nums'])
    print(res['type'])

if __name__ == "__main__":
    asyncio.run(main())