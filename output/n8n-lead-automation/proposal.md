# Proposal: Automatic lead capture and routing for Brightstone Home Renovations

Hi Brightstone team,

## Every website lead, in the CRM and with the right rep

Most of your new work comes through your website, but every lead waits in a shared inbox until someone copies it into the CRM by hand, often the next morning or later.

Some leads are missed or entered twice, nobody can see which form they came from, and half arrive without a postcode or project type, so reps chase details instead of quoting.

## How we would solve it

We'd build this in n8n, which you already use:

1. **Capture every form.** Your main contact form, "get a quote" form and loft conversion landing page feed n8n automatically.
2. **Tidy each lead.** Names and postcodes are cleaned up, the project type becomes a tag and the postcode is checked. Missing details are flagged, not guessed.
3. **Stop duplicates.** Each lead is checked against existing ones (for example by email and phone).
4. **Route to the right rep.** The lead goes into your CRM, assigned to the rep for that region, with its source form recorded.
5. **Alert the rep** as soon as the lead arrives.

The weekly summary of leads by source can be added once the main flow is running. We'll also check together whether your n8n is the cloud or self-hosted version.

[Add 1 or 2 relevant examples from your portfolio here.]

## How we would work together

- A discovery call with your office manager, who knows the process best.
- We build in stages, testing each with made-up leads before real ones go through.
- Short, plain-English updates as we go, and a simple walkthrough at the end.

## A few questions before we start

1. Which CRM do you use? We'll also need API access (a key that lets n8n add leads), shared securely rather than by email.
2. What tool runs each of your three forms, especially the loft conversion landing page?
3. How do you decide which regional rep gets a lead today? A list of postcodes per region would be ideal.
4. How should reps be alerted: by email or by a chat tool? If chat, which one?
5. For enrichment, is a free, basic check (postcode check and project tags) enough, or would you consider a paid data service that charges per lead?

## Pricing and next steps

Pricing will be confirmed after a short discovery call, once we have the answers above. Just reply with a couple of times that suit your office manager.

Best,

[Your name]
