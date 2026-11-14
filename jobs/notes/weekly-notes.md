# notes - brightstone n8n leads job

done
- got access to n8n finally (it's self hosted btw, on their old dev's server)
- webhook set up for main contact form + quote form, both firing ok in test
- tidy step: trims names, fixes postcode formatting, maps project type dropdown to tags
- dupe check working on email + phone, tested w/ fake leads, caught all 5 dupes
- added "source" field so we know which form it came from

next
- loft landing page form (diff form builder?? need to check)
- connect to CRM once they confirm which one + send API access
- rep assignment by region, need postcode -> region list from office mgr
- instant notification to rep (email or chat? ask)

blocker
- still no CRM name or API key. asked twice. can't push leads anywhere til we have it

decision needed
- enrichment: do they want to pay for a paid enrichment service (more data, per-lead cost) or keep it free/basic (postcode check + tags only)? need answer before i build that bit

misc
- office mgr v helpful, quick replies
- server is a bit slow, might mention later
