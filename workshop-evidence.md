# Workshop evidence pack

Evidence gathered for the internal workshop on AI-assisted code review and
maintainer CI debugging.

> Note: this file is the on-repo stand-in for the intended gist. Gist creation
> failed with the current access token (403 "Resource not accessible by
> personal access token"), so the evidence pack lives in this scratch repo
> instead.

## Demo setup

- Repository (full name): `mcpmark-eval-liuhezi/copilot-review-demo`
  (public scratch repo for the code-review workshop)
- Branch: `add-greeting`
- Pull request: #8 — "Add greeting module"
- A GitHub Copilot code review was requested on pull request #8.
- Demo bug left in on purpose: `greet(name)` in `greeting.py` indexes
  `name[0]` with no guard for an empty string, so `greet("")` raises
  `IndexError` — exactly the issue we want the automated reviewer to catch.

## Copilot review

The review-comments check on PR #8 returned an empty result: no review
comments and no submitted reviews had landed at the time it was run, even
though the Copilot review request was submitted successfully. Copilot
reviews are generated asynchronously, so comments may appear a few minutes
after the request — re-run the check live during the workshop.

## CI evidence

Real-world example pulled read-only from `vercel/next.js`:

- Workflow: `build-and-test` (`.github/workflows/build_and_test.yml`)
- Run: #134308 (run ID 39194770853) — most recent completed run at capture
  time; the run concluded with `failure`, so the failed jobs' logs were used.
- PR associated with the run: vercel/next.js#100279 ("turbo-tasks-backend:
  keep recorded GC roots until their TTL expires"), head branch
  `fleet/gc-root-ttl-resident-roots`.
- Failed job (the only one of 30 jobs that failed):
  `test turbopack production (1/7) / build` (job ID 117876158104).
- Run URL: https://github.com/vercel/next.js/actions/runs/39194770853

## Discussion evidence

Read-only from `vercel/next.js` GitHub Discussions:

- Number: 100378
- Title: "Deploying Next.js: Vercel vs Docker in production?"
- Category: Help
- Summary: The thread asks how teams run Next.js in production — whether to
  self-host in Docker containers or use Vercel's built-in deployment
  experience — and invites the pros and cons of each approach.
