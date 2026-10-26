# Good Manager / Great Manager

A reusable scorecard-driven workshop engine: select one of nine scorecards from the Open Leadership & Management Cookbook or import Markdown/JSON, create a database-backed session, share a long random ID, teach one behavior per slide, and release personal self-versus-peer reports.

## Included

- Account-free create/join flow; no session directory or session history.
- 128-bit random session IDs; separate facilitator and participant capability keys.
- D1 persistence for sessions, immutable scorecard snapshots, roster, progress, ratings, and private reflection notes.
- Facilitator-controlled slides with 3-second polling on participant devices.
- 1–5 scoring and explicit “not enough evidence”; ratings lock when reports release.
- Equal-weight behavior means, matched-behavior self/peer gaps, counts, ranges, strengths, development areas, and possible blind spots.
- Markdown / JSON validation with a preview and structural warnings.
- One renderer and report engine for every scorecard; presentation mode and responsive layouts.
- Fictional sample session, JSON scorecard and report export.

## From a fresh cookbook checkout

```bash
git clone https://github.com/dobromirmontauk/open-leadership-management-cookbook.git
cd open-leadership-management-cookbook/recipes/management/increasing_the_capacity_to_win/growing/expectations/scorecards/src
corepack enable
```

Use the pnpm version pinned in `package.json`. Node.js 24 LTS is recommended so the SQLite-backed tests also run. No ChatGPT or Sites credentials are needed for standalone Cloudflare deployment.

## Local development

```bash
pnpm install --frozen-lockfile
pnpm db:generate # only after changing schema; initial migration is already included
pnpm build
node --import ./scripts/sites-env.mjs ./node_modules/wrangler/bin/wrangler.js d1 migrations apply DB --local --config dist/server/wrangler.json --persist-to .wrangler/state
pnpm dev
```

The development command prints its local address. Managed Sites previews use the platform preview launcher instead. Run `pnpm typecheck` and `pnpm test` for checks.

## Scorecard format

Markdown:

```markdown
1. Execution
    1. Makes realistic commitments and meets them.
    2. Identifies dependencies early.
2. Delegation
    1. Gives people clear ownership.
```

Also supported: `## Execution` headings with bullet lists. Introductory text is omitted with a warning; deeper nested bullets combine with their parent with a warning. Empty sections and inconsistent indentation are errors. The cookbook's 4–6 dimensions and 3–5 behaviors per dimension are recommendations, surfaced as warnings rather than forced limits.

JSON:

```json
{
  "title": "Manager scorecard",
  "sections": [
    {
      "title": "Execution",
      "items": [{ "text": "Makes realistic commitments and meets them." }]
    }
  ],
  "scale": ["Not yet demonstrated", "Needs improvement", "Does well", "Amazing", "Exceptional"]
}
```

Scale is optional; defaults to the shared workshop scale. Each session stores a snapshot so template changes never alter existing class reports. Imported templates are remembered on the importing device; a created session's snapshot is durable and shared across devices. Blank/TODO items from cookbook drafts are excluded. Source text, GitHub URL, and source SHA are retained in `data/sources.json`.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for Cloudflare credentials, D1 provisioning, dry runs, migrations, and deployment commands. Remote deployment has not been configured with personal Cloudflare credentials.
