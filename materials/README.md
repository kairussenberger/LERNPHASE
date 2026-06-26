# materials/ — your raw study files (kept local)

Drop your **lecture PDFs, slides, past-exam papers, scanned scripts, and your own summaries** in here. Organize it however you like:

```
materials/
├── electronic-circuits/
│   ├── lecture-01.pdf
│   ├── past-exam-2024.pdf
│   └── my-summary.pdf
├── discrete-math/
│   └── ...
└── ...
```

## Everything in here is git-ignored

The repo's [`.gitignore`](../.gitignore) excludes the contents of this folder (everything except this README). That's deliberate:

- Course PDFs are often **large** and **copyrighted** — they don't belong in a public repo.
- Your scanned notes are **personal**.

So you can keep all your raw material right next to your plan without it ever being pushed to GitHub.

## How to use it

1. Put files here.
2. **Reference them by name** from your subject docs in [`../subjects/`](../subjects/), e.g. *"see `past-exam-2024.pdf`"*.
3. **Decode** them into a playbook: read once, then write down what actually shows up and what to drill. The decoded plan is what's worth committing — the raw files stay local.

See the top-level [README](../README.md) → *Import your files & summaries* for the full workflow.
