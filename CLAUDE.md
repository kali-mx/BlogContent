# BlogContent: CTF/TryHackMe Writeup Pipeline

This repo is kali-mx's public writeup site, served via GitHub Pages at
**https://kali-mx.github.io/BlogContent/**. It is linked from the "Writeups"
card on the main portfolio, **https://kali-mx.github.io/** (repo:
`kali-mx/kali-mx.github.io`), whose index.html already points here. That
link doesn't need touching again unless the card text/URL changes.

The repo predates this pipeline and still holds older PDF/Markdown
writeups at the root (not yet migrated). New writeups go through the
process below instead of being added in that old format.

## The process, start to finish

1. **User pastes a raw writeup** (usually Markdown, straight from their
   own notes: a TryHackMe room walkthrough with phases/sections, commands,
   command output, and either a flag or a set of graded Q&A answers).

2. **Build a standalone HTML page** at `writeups/<slug>.html`, where
   `<slug>` is a short kebab-case name for the room (e.g. `portal-drop`,
   `jackpot`, `o365-intrusion`). It's a full `<!DOCTYPE html>` document
   (not an Artifact fragment), linking:
   - Google Fonts: `JetBrains Mono` (headings/code/mono bits) + `Source Sans 3` (body)
   - `../assets/style.css`, the shared stylesheet (see below)

   Structure, reusing the components already in `assets/style.css`:
   - `.eyebrow` back-link to `../index.html`, then `TryHackMe`
   - `<h1>` + `.dek` (one-sentence hook) + `.meta-row` pills (room, category, tools)
   - `.brief` box: 1-2 sentence scenario setup
   - Optional `.skills` grid as a background/glossary section if the room
     needs upfront concept explanations (XFS, SIEM, FNV-1a, etc.)
   - `.steps` timeline: each `.step` is numbered, has a `.step-title`,
     prose, a `<pre><code>` block for commands/output where useful, and a
     `.notebook` callout at the end explaining **why** the technique
     works, not just what was typed. This "why this works" note on every
     step is the whole pedagogical point, don't skip it.

     **Hard rule: every `<pre><code>` block must be verbatim from the
     source, not a paraphrase, not a reconstruction, not a placeholder.**
     Real commands with real flags, real IPs/hashes/output exactly as
     captured in the source screenshots or notes, never `<victim>`,
     `<target-ip>`, or similar stand-ins unless the source itself never
     actually showed the real value. A step whose only evidence is a
     sentence describing what happened, with no copyable command behind
     it, has failed the one job this site exists to do: let a learner
     reproduce the steps. This regressed once already (the first pass on
     Hacker of the Hill summarized the attack in prose with 2-3 token
     code blocks instead of transcribing the ~20 real commands and
     outputs sitting right there in the source PDF), caught by the user
     reading the published page and noticing it "wasn't reproducible."
     Before considering a writeup done, count the `<pre><code>` blocks
     against the number of distinct commands/outputs actually shown in
     the source, they should roughly match. If a PDF's source is
     screenshots, read every page at full resolution and transcribe the
     terminal/browser text directly, don't summarize what the screenshot
     shows.
   - Optional "Full Attack Chain" `<pre>` ASCII tree summarizing the
     timeline (nice visual recap, not required)
   - Optional `table.ref` (see style.css) for a "Tools Used" reference table
   - `.skills` grid again for "Takeaways" / "What I Practiced" (lessons
     that generalize beyond this one room)
   - `<footer>` with a link back to the room on tryhackme.com

3. **Content policy, always apply this:**
   - **Never publish the literal flag.** Full stop, in code output, in
     prose, anywhere.
   - **Never publish an "answer key."** If the source material has a
     dedicated Q&A answer table/list (like Portal Drop did), drop that
     section entirely, the step-by-step narrative already demonstrates
     the methodology.
   - **Calibrate how much to generalize specific values** (IPs, exact
     timestamps, filenames, usernames) based on how 1:1 they map to a
     graded question:
     - If the room has one flag and the specifics are *evidence found
       along the way* (Portal Drop, Jackpot), keep them in the prose.
       That's normal, expected writeup depth and matches real public
       CTF writeups.
     - If the room is Q&A-dense and nearly every sentence states an
       answer to a specific numbered question (O365 Intrusion), go
       further: generalize the atomic values themselves ("a Windows
       machine" not "Windows10", "roughly eleven minutes" not an exact
       duration, `<victim>` placeholders in shown SPL/queries) while
       keeping every query, technique, and "gotcha" explanation intact.
       Tell the user which calibration you used and that you're willing
       to adjust it.
   - **No em dashes, anywhere**, not the unicode `—` character, not
     `&mdash;`, not a `--` stand-in either. This is a firm, general
     writing-style preference for this user (reads as an obvious AI
     writing tell), not unique to writeups. Restructure with periods,
     commas, or colons instead. Always `grep -n "—\|&mdash;"` the new
     file before committing, and watch for plain `--` too since source
     drafts often use that as a dash substitute.

4. **Add it to `index.html`**: a new `.writeup-card` `<a>` block inside
   `.writeup-list`, with a `.wc-title`, one-sentence `.wc-dek`, and
   `.wc-meta` pills. Put new writeups at the **top** of the list (most
   recent first).

5. **Commit and push.** Git identity needs setting per fresh clone (this
   sandbox has no persistent git config):
   ```bash
   GH_ID=$(gh api user --jq '.id')
   git config user.name "kali-mx"
   git config user.email "${GH_ID}+kali-mx@users.noreply.github.com"
   ```
   Use the GitHub no-reply email with the account's real numeric ID
   (fetched above, don't hardcode it or let a shell `$UID` collision
   silently substitute the Linux UID instead). A wrong numeric ID still
   pushes fine but won't show as a verified/attributed commit on GitHub.

   GitHub auth: `gh auth status` to check; if not logged in, the user
   needs to run `gh auth login` themselves in a real terminal (device
   flow needs an interactive TTY this sandbox doesn't have). Once
   authenticated, `gh auth setup-git` wires the credential helper so
   plain `git push` works.

6. **Verify the Pages build**, don't just assume the push worked:
   ```bash
   gh api repos/kali-mx/BlogContent/pages/builds/latest --jq '.status'
   ```
   Poll every ~10s until it says `built` (first-time Pages enablement is
   already done on this repo, no need to redo
   `gh api -X POST repos/kali-mx/BlogContent/pages ...`). Then spot-check
   the live URL, either `WebFetch` for a text sanity check or
   `omarchy capture screenshot` + `Read` if visual confirmation matters
   (this user runs Omarchy/Hyprland; see the Omarchy skill for capture
   commands if that's relevant in a given session).

## Shared design system (`assets/style.css`)

Token-based light/dark theme (`:root`, `prefers-color-scheme: dark`,
`[data-theme]` overrides), cyan/teal accent (`--accent`), semantic
severity colors (`--sev-high/med/low`) borrowed from EDR-style High/
Medium/Low conventions, dark terminal-style code blocks regardless of
page theme. Reuse these tokens and existing classes rather than
inventing new ad hoc styles per writeup, the whole point is that every
writeup on this site looks like one coherent system. If a genuinely new
component is needed (like `table.ref` was, added for Jackpot's Tools
table), add it to the shared stylesheet, not inline in the page.

## Known gaps / not yet done

- The root-level PDF/Markdown source files are left in place after
  migration (not deleted), both as a backup and because the user hasn't
  asked for cleanup. A handful of originally-skipped files (tool demo
  video stubs, an unrelated Django tutorial, loose scripts/images)
  deliberately have no corresponding writeup, see the git log around
  the initial migration commits for the full skip list and why.
- No RSS/sitemap, no tagging/filtering on the index, it's just a flat
  reverse-chronological list. Fine for now, revisit if the list grows
  large.
