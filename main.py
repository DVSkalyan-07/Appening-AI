import os
import asyncio
import nest_asyncio

# Enable async support for execution environments
nest_asyncio.apply()

from crewai import Agent, Task, Crew, Process, LLM

def run_crew():
    # Fetch API Key from environment variable
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY or GOOGLE_API_KEY in your environment variables.")

    # Initialize Gemini model via LiteLLM routing format
    llm = LLM(
        model="gemini/gemini-1.5-flash",
        api_key=api_key,
        temperature=0.2
    )

    # 1. Define Agents
    research_agent = Agent(
        role="Agentic AI Specialist",
        goal="Identify key metrics, multi-agent patterns, and architectural requirements for agentic AI projects.",
        backstory="An expert AI Architect specializing in multi-agent orchestration, tool integration, and design patterns.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    developer_agent = Agent(
        role="Senior AI Systems Engineer",
        goal="Synthesize business objectives into executable, production-ready Python code implementing multi-agent workflows.",
        backstory="A developer skilled at converting agentic workflow designs into clean, runnable Python code structures.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    verifier_agent = Agent(
        role="Verification & Compliance Evaluator",
        goal="Audit generated code and architectures against performance metrics, safety, and operational standards.",
        backstory="Validates system execution, checks for edge cases, and verifies business value delivery.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # 2. Define Tasks
    task_extract = Task(
        description="Summarize the core architectural requirements, key performance metrics, and agent interaction patterns for an Agentic AI assignment.",
        expected_output="A structured summary of architectural requirements, agent roles, and evaluation metrics.",
        agent=research_agent
    )

    task_code = Task(
        description="Construct a complete working multi-agent interaction flow in Python using Planner, Worker, and Verifier roles.",
        expected_output="Fully executable Python code implementing the multi-agent orchestration system.",
        agent=developer_agent
    )

    task_verify = Task(
        description="Audit the generated solution to ensure alignment with production standards, error handling, and operational quality.",
        expected_output="An executive evaluation report validating performance metrics and functional completeness.",
        agent=verifier_agent
    )

    # 3. Assemble Crew
    agent_crew = Crew(
        agents=[research_agent, developer_agent, verifier_agent],
        tasks=[task_extract, task_code, task_verify],
        process=Process.sequential,
        verbose=True
    )

    # 4. Execute Workflow
    result = agent_crew.kickoff()
    
    print("\n==========================================")
    print("     FINAL MULTI-AGENT EXECUTIVE REPORT   ")
    print("==========================================\n")
    print(result)

if __name__ == "__main__":
    run_crew()
