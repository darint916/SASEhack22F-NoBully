# Why you bully me

## Run
1. Activate the `venv`
2. cd to `proxy`
3. Install libs by `pip install -r requirements.txt`
4. Run `main.py`

## Schema
```javascript
{
    // List of domains in regular expression
    domains: [".*instagram\.com.*"],

    // List of words to block, Maybe Regex?
    blockedWords: [],
}
```

```javascript
{
    name: "<Intercepter Name>",

    activated: true,

    intercepted: [{
        'message': '<The message that has been intercepted: str>',
        'domain': '<The domain that was sent from: str>',
        'reason': '<Which rule did this trigger: str>',
        'timestamp': '<Timestamp for the event>'
    }]
}
```
