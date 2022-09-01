# Video Member ship

User

## Content via Vimeo

Video:
   - viemo_id

BlogPost:
  - title
  - description


Newsletter:


Content
  - content: video / blog post / newsletter / podcast
  - data:
       video: {vimeo_video_id: 34343434}
       blog post: { title, description, image }
  - Pricing (ManyToMany)

## Subscription


Pricing
  - price per month
  - currency
  - id
  - name (basic/pro/business)

Merchant / Subscription
    - User
    - stripe_subscription_id
    - basic / pro
    - status (active / canceled / past_due / trialing)
    - Pricing (FK)
