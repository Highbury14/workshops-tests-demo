from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.loop_agent import LoopAgent

coordinator_agent = Agent(
  model="gemini-3.6-flash",
  name="coordinator_agent",
  description="This agent coordinates with the user by receiving their requests and beginning the process to create a personalised 10-days study-plan.",
  instruction="""
Receive the student's request and pass it to the planning_agent .
You should identify the following information from the student's request :
- Subjects to study for the exam
- Exam-date / number of days remaining for the exam
- Exam-topics to study
- Current level of study-preparation for the exam
- Available study-time
""".strip()
)

planning_agent = Agent(
  model="gemini-3.6-flash",
  name="planning_agent",
  instruction="""
Prepare the requirements for creating the personalised 10-day study-plan and for starting three independent analysis tasks.
You should pass the relevant information to the following three agents :
- topic_agent
- practice_agent
- scheduler_agent
""".strip()
)

topic_agent = Agent(
  model="gemini-3.6-flash",
  name="topic_agent",
  instruction="""
Analyze the study-topics provided by the student.
For each study-topic, identify the following information :
- Priority-level: High / Medium / Low
- Difficulty-level in studying the topic: Hard / Medium / Easy
- Recommended study focus-level for the topic: In-depth / Moderate / Overview
""".strip()
)

practice_agent = Agent(
  model="gemini-3.6-flash",
  name="practice_agent",
  instruction="""
Decide how much practice should be done for each study-topic.
Calculate the number of practice questions to be solved for each topic based on its priority and difficulty.
Recommend one or more of the following types of practice required, for each topic :
- Concept Questions
- Coding Problems
- Mixed Practice
- Mock Test
""".strip()
)

scheduler_agent = Agent(
  model="gemini-3.6-flash",
  name="scheduler_agent",
  instruction="""
Convert the available study-time into a realistic 10-days daily-schedule.
Schedule a day-wise 10-days study-plan.
Include revision and practice of all study-topics, in the study-plan.
""".strip()
)

plan_writer_agent = Agent(
  model="gemini-3.6-flash",
  name="plan_writer_agent",
  instruction="""
Receive the outputs from the following three agents :
- topic_agent
- practice_agent
- scheduler_agent
Combine the received outputs into one complete personalized 10-day study-plan.
The final personalised 10-days study-plan should include:
- Day-wise 10-days schedule
- Topics to study
- Practice to complete
- Revision
- Mock-test and final preparation
""".strip()
)

reviewer_agent = Agent(
  model="gemini-3.6-flash",
  name="reviewer_agent",
  instruction="""
Check the draft of the personalised 10-day study-plan, received from the plan_writer_agent .
You should verify the following points in the draft study-plan received from the plan_writer_agent :
- Are all topics covered in the study-plan ?
- Does the study-plan fit within the available study-time ?
- Is sufficient practice included in the study-plan ?
- Is revision included in the study-plan ?
- Is the final day of the study-plan suitable for exam preparation ?
""".strip()
)

parallel_team = ParallelAgent(
  name="research_team",
  description="These three agents must execute independently and in parallel.",
  sub_agents=[
    topic_agent,
    practice_agent,
    scheduler_agent
  ]
)

review_loop = LoopAgent(
  name="review_loop",
  description="""
The review process should run for maximum 2 iterations.
If the plan is satisfactory in the first iteration, it can directly be approved as the final 10-days study-plan. The second iteration is only required if the plan is not satisfactory in the first iteration.
""".strip(),
  sub_agents=[
    plan_writer_agent,
    reviewer_agent
  ],
  max_iterations=2
)

root_agent = SequentialAgent(
  name="report_pipeline",
  description="""
A multi-agent system that helps a student-user prepare for an upcoming examination.
The system should analyze the student's requirements and generate a personalized 10-day study-plan.
""",
  sub_agents=[
    coordinator_agent,
    planning_agent,
    parallel_team,
    review_loop
  ]
)
