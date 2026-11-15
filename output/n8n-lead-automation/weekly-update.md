# Weekly update: Brightstone lead automation

Hi Brightstone team,

Good progress this week: two of your three forms are connected, and the clean-up and duplicate checks work in testing. Thanks to your office manager for the quick, helpful replies.

## Done

- We now have access to your n8n (it's self-hosted, on your previous developer's server).
- The main contact form and "get a quote" form are captured automatically. Both worked in testing.
- Each lead is tidied as it arrives: names trimmed, postcodes formatted and the project type turned into a tag.
- A duplicate check compares email and phone number. In a test using made-up leads, it caught all 5 duplicates we included.
- Every lead now records which form it came from.

## Next

- Add the loft conversion landing page form, once we've checked which form builder it uses.
- Connect everything to your CRM.
- Assign leads to regional reps by postcode. Could your office manager send us the list of which postcodes belong to which region?
- Notify the rep as soon as a lead arrives. Would your reps prefer email or a chat message?

## Blockers

- **CRM details:** leads can't go into your CRM until you confirm which CRM you use and arrange API access for us (a key that lets n8n send leads into it). Please don't send keys or passwords by email. We'll suggest a secure way to share access.

## One decision needed

**Lead enrichment** (adding extra details to each lead automatically):

1. **Keep it free and basic:** a postcode check plus project type tags. No additional enrichment-service costs.
2. **Use a paid enrichment service:** more details per lead, charged per lead. We'd confirm the cost with you before setting anything up.

We'll hold off on this part until we hear which you prefer.

Thanks again, and just reply with any questions.

Best,

[Your name]
