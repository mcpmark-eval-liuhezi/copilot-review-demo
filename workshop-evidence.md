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

## Raw log tail

Tail of the failed job `test turbopack production (1/7) / build`
(job ID 117876158104) from vercel/next.js `build-and-test` run #134308
(run ID 39194770853):

```text
2026-10-19T03:44:14.4365985Z   FNM_NODE_DIST_MIRROR: https://nodejs.org/dist
2026-10-19T03:44:14.4366291Z   FNM_ARCH: arm64
2026-10-19T03:44:14.4366523Z   FNM_DIR: /home/runner/.local/share/fnm
2026-10-19T03:44:14.4366811Z   FNM_LOGLEVEL: info
2026-10-19T03:44:14.4367055Z   FNM_COREPACK_ENABLED: true
2026-10-19T03:44:14.4367319Z   FNM_RESOLVE_ENGINES: true
2026-10-19T03:44:14.4367665Z   FNM_MULTISHELL_PATH: /run/user/1001/fnm_multishells/2901_1792380733379
2026-10-19T03:44:14.4368109Z   DATADOG_CI_PATH: /tmp/nextjs-ci-bin-datadog-ci-v5.12.1
2026-10-19T03:44:14.4368439Z ##[endgroup]
2026-10-19T03:44:14.5559057Z With the provided path, there will be 13 files uploaded
2026-10-19T03:44:14.5563308Z Artifact name is valid!
2026-10-19T03:44:14.5563763Z Root directory input is valid!
2026-10-19T03:44:14.9128033Z Uploading artifact: test-playwright-snapshots-test-turbopack-production-react--1-7.zip
2026-10-19T03:44:14.9161751Z Beginning upload of artifact content to blob storage
2026-10-19T03:44:15.4724138Z Uploaded bytes 404550
2026-10-19T03:44:15.5413953Z Finished uploading artifact content to blob storage!
2026-10-19T03:44:15.5414558Z SHA256 digest of uploaded artifact is a17dbdd6d1faf39a5712c7a6dff4612d5f5de3650ba152c962a9c958f0aedd47
2026-10-19T03:44:15.5415304Z Finalizing artifact upload
2026-10-19T03:44:15.9485989Z Artifact test-playwright-snapshots-test-turbopack-production-react--1-7 successfully finalized. Artifact ID 12162116819
2026-10-19T03:44:15.9487136Z Artifact test-playwright-snapshots-test-turbopack-production-react--1-7 has been successfully uploaded! Final size is 404550 bytes. Artifact ID is 12162116819
2026-10-19T03:44:15.9489572Z Artifact download URL: https://github.com/vercel/next.js/actions/runs/39194770853/artifacts/12162116819
2026-10-19T03:44:15.9658388Z Post job cleanup.
2026-10-19T03:44:16.0393677Z [command]/usr/bin/git version
2026-10-19T03:44:16.0430625Z git version 2.55.0
2026-10-19T03:44:16.0460577Z Copying '/home/runner/.gitconfig' to '/home/runner/work/_temp/d87733a5-bb00-40b6-96b6-bd870de61642/.gitconfig'
2026-10-19T03:44:16.0471201Z Temporarily overriding HOME='/home/runner/work/_temp/d87733a5-bb00-40b6-96b6-bd870de61642' before making global git config changes
2026-10-19T03:44:16.0472014Z Adding repository directory to the temporary git global config as a safe directory
2026-10-19T03:44:16.0477823Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/next.js/next.js
2026-10-19T03:44:16.0510383Z Removing SSH command configuration
2026-10-19T03:44:16.0552894Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all core.sshCommand || :"
2026-10-19T03:44:16.0891866Z Removing HTTP extra header
2026-10-19T03:44:16.0898270Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-10-19T03:44:16.0938555Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all http.https://github.com/.extraheader || :"
2026-10-19T03:44:16.1263456Z Removing includeIf entries pointing to credentials config files
2026-10-19T03:44:16.1271521Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-10-19T03:44:16.1306548Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-10-19T03:44:16.1768212Z Evaluate and set job outputs
2026-10-19T03:44:16.1773635Z Set output 'input_step_key'
2026-10-19T03:44:16.1775915Z Cleaning up orphan processes
```

Note for the workshop: the tail shows the job's post-failure behavior —
uploading the Playwright snapshot artifacts that preserve the failure
evidence, then runner cleanup — which is exactly the trail a maintainer
follows when triaging a red build (start from the failed job, then open the
uploaded snapshot artifact to inspect what actually broke).
