# 50-Day Gen AI Agent Mastery Plan
24 hands-on projects · 6 phases · from LLM basics to production-safe multi-agent systems

---

## Topics Covered
Prompt Engineering, LLM APIs (OpenAI / Anthropic), LangChain & LlamaIndex, Vector Databases, RAG Systems, Function Calling & Tool Use, AI Agents & ReAct, Multi-Agent Frameworks, Streaming & Latency, Evaluation & Evals, LangGraph / CrewAI, Multimodal (Vision), Deployment & Monitoring, Agent Safety & Guardrails, Observability & Tracing, MCP (Model Context Protocol), Cost & Latency Optimization, Async / Parallel Agents, Fine-tuning (QLoRA)

---

## Phase 1 — LLM Foundations & Prompt Engineering (Days 1–10)

**Project 1 — Smart CLI Chatbot** · Days 1–2 · LLM API
Build a terminal chatbot using OpenAI/Anthropic API with multi-turn memory, streaming output & system prompts.

**Project 2 — Prompt Engineering Playground** · Days 3–4 · Prompting
Build a UI to compare zero-shot vs few-shot vs chain-of-thought on your own tasks with scoring.

**Project 3 — AI Document Summarizer** · Days 5–6 · LLM API
Upload PDFs/text, chunk intelligently, summarize with map-reduce & compare different summarization strategies.

**Project 4 — Structured Data Extractor** · Days 7–8 · Function Calling
Extract structured JSON from unstructured text (invoices, emails, articles) using function calling / tool use.

**Project 5 — LLM Eval Harness** · Days 9–10 · Evals
Build an evaluation pipeline — define metrics, test prompts at scale, track regressions across model versions.

---

## Phase 2 — RAG & Vector Databases (Days 11–20)

**Project 6 — Personal Knowledge Base** · Days 11–12 · RAG
Ingest your notes/docs into a vector DB (Chroma/Pinecone), embed with OpenAI, answer questions with citations.

**Project 7 — Codebase Q&A Bot** · Days 13–14 · RAG
Index a GitHub repo, chunk by function/class, answer "how does X work?" questions with code snippets.

**Project 8 — Hybrid Search Engine** · Days 15–16 · RAG + BM25
Combine dense vector search + sparse BM25 with re-ranking. Compare retrieval quality vs naive RAG.

**Project 9 — Conversational RAG with Memory** · Days 17–18 · RAG + Memory
Add conversation history, query rewriting, and follow-up question handling to your RAG pipeline.

**Project 10 — RAG Evaluation Suite** · Days 19–20 · Evals
Evaluate RAG with RAGAS metrics (faithfulness, answer relevancy, context recall) and visualize results.

---

## Phase 3 — AI Agents, Tool Use & Observability (Days 21–34)

**Project 11 — ReAct Web Research Agent** · Days 21–22 · Agent
Build a ReAct loop agent that can search the web, read pages, and synthesize multi-step research reports.

**Project 12 — Code Interpreter Agent** · Days 23–24 · Agent + Tools
Agent that writes, executes, and debugs Python code in a sandbox to solve data analysis tasks end-to-end.

**Project 13 — Personal Task Automation Agent** · Days 25–26 · Agent + APIs
Agent with tools: Gmail, Calendar, Notion. Give it a goal like "schedule my week" and watch it plan.

**Project 14 — LangGraph Stateful Agent** · Days 27–28 · LangGraph [UPDATED]
Rebuild your research agent in LangGraph — add branching, human-in-the-loop, state persistence, and async parallel tool execution (fan-out/fan-in patterns).

**Project 15 — Agent Memory System** · Days 29–30 · Memory
Give your agent short-term (in-context), long-term (vector), and episodic memory. Watch it learn from past sessions.

**Project 16 — Agent Observability & Tracing** · Days 31–32 · Observability [NEW]
Set up LangSmith tracing on your existing agents. Build a custom trace logger, visualize tool-call chains, identify where agents fail and why.

**Project 17 — Agent Safety & Guardrails** · Days 33–34 · Safety [NEW]
Add prompt injection defense, output validation (Pydantic), sandboxed tool execution, and human-approval gates. Attack your own agent and patch it.

---

## Phase 4 — Multi-Agent Systems, MCP & Optimization (Days 35–45)

**Project 18 — CrewAI Research Team** · Days 35–36 · Multi-Agent
Orchestrate a crew: Researcher + Analyst + Writer agents that collaborate to produce a full industry report.

**Project 19 — Autonomous Software Engineer** · Days 37–39 · Multi-Agent
Multi-agent system: Planner → Coder → Reviewer → Tester agents that take a feature spec and ship working code (3 days).

**Project 20 — MCP Integration** · Days 40–41 · MCP [NEW]
Build a custom MCP server that exposes tools to your agent. Connect it to a real external service (GitHub, Notion, or a DB). Understand why MCP is becoming the industry standard for agent–tool connectivity.

**Project 21 — Cost & Latency Optimization** · Days 42–43 · Optimization [NEW]
Implement model routing (cheap → expensive), semantic caching, token budgeting, and batching. Measure cost and latency before/after — aim for 50%+ reduction.

**Project 22 — Multimodal Vision Agent** · Days 44–45 · Multimodal
Agent that takes screenshots, describes UI, fills forms, and navigates websites using vision + tool calls.

---

## Phase 5 — Capstone Production System (Days 46–50)

**Project 23 — Production AI Agent Platform** · Days 46–50 · Capstone [UPDATED]
Deploy a full-stack multi-agent system: FastAPI backend, streaming frontend, vector DB, auth, LangSmith tracing, safety guardrails, MCP tool integration, cost dashboard, CI/CD — everything production-grade.

---

## Phase 6 — Fine-tuning (Days 51–53)

**Project 24 — Fine-tuning Pipeline** · Days 51–53 · Fine-tuning
Fine-tune a small model (Mistral / Llama) using QLoRA on a domain dataset. Compare performance vs prompting the base model. Covers: dataset preparation, training run, LoRA adapter merging, evaluation vs base model.

---

## Change Log vs Original 45-Day Plan
- Phase 3 expanded: added Observability & Tracing (Project 16) and Safety & Guardrails (Project 17)
- Phase 4 expanded: added MCP Integration (Project 20) and Cost & Latency Optimization (Project 21)
- LangGraph project updated to include async parallel execution and fan-out/fan-in patterns
- Capstone updated to include tracing, guardrails, MCP, and cost dashboard
- Fine-tuning moved to Phase 6 after the capstone (Days 51–53)
- Total: 50 days core + 3 days fine-tuning = 53 days, 24 projects
