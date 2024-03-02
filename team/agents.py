from textwrap import dedent
from crewai import Agent


class WebDevelopmentAgents:
    def senior_backend_engineer_agent(self, framework):
        return Agent(
            role='Senior Backend Engineer',
            goal='Create software as needed',
            backstory=dedent(f"""\
			You are a Senior Backend Engineer at a leading tech think tank.
			Your expertise in programming in framework {framework}. and do your best to
			produce perfect code"""),
            allow_delegation=False,
            verbose=True
        )

    def senior_frontend_engineer_agent(self, framework):
        return Agent(
            role='Senior Frontend Engineer',
            goal='Create software as needed',
            backstory=dedent(f"""\
			You are a Senior Frontend Engineer at a leading tech think tank.
			Your expertise in programming in {framework}. and do your best to
			produce perfect code"""),
            allow_delegation=False,
            verbose=True
        )

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
            goal='create prefect code, by analizing the code that is given for errors',
            backstory=dedent("""\
			You are a software engineer that specializes in checking code
			for errors. You have an eye for detail and a knack for finding
			hidden bugs.
			You check for missing imports, variable declarations, mismatched
			brackets and syntax errors.
			You also check for security vulnerabilities, and logic errors"""),
            allow_delegation=False,
            verbose=True
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role='Chief Software Quality Control Engineer',
            goal='Ensure that the code does the job that it is supposed to do',
            backstory=dedent("""\
			You feel that programmers always do only half the job, so you are
			super dedicate to make high quality code."""),
            allow_delegation=True,
            verbose=True
        )
