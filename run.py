from dotenv import load_dotenv

from team.agents import WebDevelopmentAgents
from team.tasks import WebDevelopmentTasks

load_dotenv()

from crewai import Crew

tasks = WebDevelopmentTasks()
agents = WebDevelopmentAgents()

print("## Welcome to the Web Development Crew")
print('-------------------------------')
requirements = input("What is the requirements of the system you would like to build?\n")
backend_framework = input("What is the backend framework?\n")
front_framework = input("What is the frontend framework?\n")

# Create Agents
senior_backend_engineer_agent = agents.senior_backend_engineer_agent(backend_framework)
senior_front_engineer_agent = agents.senior_frontend_engineer_agent(front_framework)
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
backend_code = tasks.backend_code_task(senior_backend_engineer_agent, requirements, backend_framework)
backend_routers = tasks.backend_routes_task(senior_backend_engineer_agent)
frontend_code = tasks.frontend_code_task(senior_front_engineer_agent, requirements, front_framework)
review_code = tasks.review_task(qa_engineer_agent, requirements, [backend_framework, front_framework])
approve_code = tasks.evaluate_task(chief_qa_engineer_agent, requirements, [backend_framework, front_framework])

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_backend_engineer_agent,
        senior_front_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        backend_code,
        backend_routers,
        frontend_code,
        review_code,
        review_code
    ],
    verbose=True
)

software = crew.kickoff()

# Print results
print("\n\n" + 50 * "#")
print("## Here is the result")
print(50 * "#" + "\n")
print("final code for the required system:")
print(software)

# i need to build signup and login functionality, the sign up should require username, password and confirmation password, and the login should user the username and password and return jwt token in case of success login
