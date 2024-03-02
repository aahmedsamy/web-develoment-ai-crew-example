from textwrap import dedent
from crewai import Task


class WebDevelopmentTasks:
    def backend_code_task(self, agent, requirements, framework):
        return Task(
            description=dedent(f"""You will create a backend using {framework}, these are the instructions:
                Instructions
                ------------
                {requirements}
                
                Your Final answer must be the full backend related code, only the backend related code and nothing else.
                """),
            agent=agent
        )

    def backend_routes_task(self, agent):
        return Task(
            description=dedent(f"""You will take the a backend code:
                Instructions
                ------------
                take the backend code and pass the routes to the frontend developer

                Your Final answer must be the routes with the request and response examples, and routes only nothing
                else.
                """),
            agent=agent
        )

    def frontend_code_task(self, agent, requirements, framework):
        return Task(
            description=dedent(f"""You will create a frontend using {framework}, these are the instructions:
                Instructions
                ------------
                {requirements}
                and use the routes from the backend and integrate.
                Your Final answer must be the full frontend related code, only the related frontend code and nothing else.
                """),
            agent=agent
        )

    def review_task(self, agent, requirements, frameworks):
        return Task(
            description=dedent(f"""\
            You are helping create a system using {frameworks}, these are the instructions:
            
            Instructions
            ------------
            {requirements}
            
            Using the code you got, check for errors. Check for logic errors,
            syntax errors, missing imports, variable declarations, mismatched brackets,
            and security vulnerabilities.
            
            Your Final answer must be the full backend and front end related code, only the backend and front end related 
            code and nothing else.
            """),
            agent=agent
        )

    def evaluate_task(self, agent, requirements, frameworks):
        return Task(
            description=dedent(f"""\
            You are helping create a system using {frameworks}, these are the instructions:
            
            Instructions
            ------------
            {requirements}
            
            You will look over the code to insure that it is complete and
            does the job that it is supposed to do.
            
            Your Final answer must be the full backend and front end related code, separated in corresponding file
            , only the backend and front end 
            related code and nothing else.
            """),
            agent=agent
        )
