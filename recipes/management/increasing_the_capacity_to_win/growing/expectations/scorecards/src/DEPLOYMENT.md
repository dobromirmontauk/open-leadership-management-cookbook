# Standalone Cloudflare deployment

This application runs on Cloudflare Workers with a D1 database. No visitor login or external identity provider is required. These scripts do not use the Sites control plane. The Sites hosting manifest remains available for the managed preview/deployment path.

From the repository root, first change into:

```bash
cd recipes/management/increasing_the_capacity_to_win/growing/expectations/scorecards/src
```

## Prerequisites

- Node.js 22.13+ (Node 24+ to run the SQLite API test suite).
- pnpm and this repository's lockfile.
- A Cloudflare account with Workers and D1 enabled.
- Either `pnpm cloudflare:login` on a developer machine or `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` in your shell / CI secret store. The token needs Workers Scripts edit and D1 edit access to the intended account. Never commit credentials.

## First deployment

```bash
pnpm install --frozen-lockfile
pnpm typecheck
pnpm test
pnpm cloudflare:login
pnpm cloudflare:create-db
```

Copy the database UUID returned by the last command, then configure your shell:

```bash
export CLOUDFLARE_ACCOUNT_ID="your-account-id"
export CLOUDFLARE_DATABASE_ID="the-d1-uuid-returned-above"
export CLOUDFLARE_WORKER_NAME="good-great-manager"
export CLOUDFLARE_DATABASE_NAME="good-great-manager"
pnpm cloudflare:dry-run
pnpm cloudflare:deploy
```

The dry run builds and validates the Worker without changing remote resources. Deploy builds, prepares `.cloudflare/wrangler.json`, applies pending D1 migrations to the specified remote database, and deploys the Worker and client assets. Wrangler prints the live workers.dev URL. Set a custom domain in Cloudflare when ready.

If the named D1 database already exists, use its UUID rather than running create-db again. Use different Worker names, database names and database UUIDs for staging and production. Database UUIDs and account IDs are configuration, not API credentials; generated configuration stays ignored anyway.

## Subsequent deployments

With the same environment variables set:

```bash
pnpm typecheck
pnpm test
pnpm cloudflare:deploy
```

For CI, set `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_DATABASE_ID`, and optional name variables in the CI environment. Run the same commands. No automatic GitHub deployment workflow is enabled.

## Database migrations

Edit `db/schema.ts`, then `pnpm db:generate`. Review and commit the generated SQL and Drizzle metadata. Treat applied migrations as immutable. Wrangler tracks pending migrations in D1; `pnpm cloudflare:migrate` applies them independently, and deploy always applies them before upload. A failed Worker deployment can still have applied migrations, so use backward-compatible schema changes.

## Sessions and privacy

Session identifiers contain 128 cryptographically random bits (32 hexadecimal characters). There is no endpoint, UI, or device history listing sessions. Keep a join URL or ID yourself. Session content and roster are visible to anyone possessing that secret ID; do not publish it. Use high entropy as capability-based access, not a claim of identity or a substitute for participant trust.

Facilitator controls require a separate random secret, stored hashed on the server and carried in a private URL fragment. Participants claim a roster seat on first join and get a separate secret remembered on that device. Claiming a name does not verify identity. The facilitator can release a seat to recover access. Personal reports reveal aggregates only; the single-rater case is explicitly labeled. Individual ratings are not returned to other participants or the facilitator. Session records currently persist until an operator removes them; no retention job is configured.

## Reference

- https://developers.cloudflare.com/d1/wrangler-commands/
- https://developers.cloudflare.com/d1/reference/migrations/
- https://developers.cloudflare.com/workers/wrangler/commands/
