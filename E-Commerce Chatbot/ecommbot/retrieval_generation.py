from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from ecommbot.ingest import ingestdata


def generation(vstore):
    try:
        retriever = vstore.as_retriever(search_kwargs={"k": 3})
        PRODUCT_BOT_TEMPLATE = """
        Your e-commerce bot is an expert in product recommendations and customer queries.
        ...
        """
        prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
        llm = ChatOpenAI()
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        return chain
    except Exception as e:
        print(f"Error initializing generation chain: {e}")
        return None


if __name__=='__main__':
    vstore = ingestdata("done")
    chain  = generation(vstore)
    print(chain.invoke("can you tell me the best bluetooth buds?"))
    
    
    
    