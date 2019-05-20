# sipit
command line interface for adding indicators and querying different aspects of SIP
```
~/.sipit.ini is required with the following configurations:
[sip]
; user that will be assigned when creating the indicator
user = rockstar5
; SIP endpoint
end_point = sip.yourdomain:4443
; api_key from SIP
api_key = 5b311126-65a1-2957-96c8-b00c5ca296dc

usage: sipit.py [-h] {query,update,create} ...

Add Indicators and query SIP

positional arguments:
  {query,update,create}
    query               query aspects of SIP. query -h for more
    update              update indicator attributes. update -h for more
    create              add indicator to SIP. create -h for more

optional arguments:
  -h, --help            show this help message and exit


usage: sipit.py create [-h] [-s STATUS] -t TYPE [--campaign CAMPAIGN]
                       [--confidence CONFIDENCE] [--impact IMPACT] -v VALUE -r
                       REFERENCE [--tags TAGS] [--source SOURCE]

optional arguments:
  -h, --help            show this help message and exit
  -s STATUS, --status STATUS
                        Status of the indicator to add - New, Analyzed,
                        Informational, Deprecated
  -t TYPE, --indicator-type TYPE
                        indicator type (URI - Path, String - PE, etc)
  --campaign CAMPAIGN   Campaign (APT32 or Oilrig)
  --confidence CONFIDENCE
                        Indicator Confidence Level
  --impact IMPACT       Indicator Impact
  -v VALUE, --value VALUE
                        Indicator Value
  -r REFERENCE, --reference REFERENCE
                        Reference from where the indicator came from - context
                        reference
  --tags TAGS           comma delimited tags
  --source SOURCE       source of the info - OSINT, DSIE, RCISC, etc

usage: sipit.py query [-h] [-t] [-s] [-c] [--tags] [-v VALUE] [-d] [--status]
                      [-id ID]

optional arguments:
  -h, --help            show this help message and exit
  -t, --types           list indicator types
  -s, --sources         list sources
  -c, --campaigns       list campaigns
  --tags                list tags
  -v VALUE, --value VALUE
                        search for an indicator value
  -d, --details         all information about an indicator value
  --status              list possible status values for indicators
  -id ID, --indicator-id ID
                        query the specific indicator information for a sip id

usage: sipit.py update [-h] [-s STATUS] -i ID

optional arguments:
  -h, --help            show this help message and exit
  -s STATUS, --status STATUS
                        update status: query --status for list of status
  -i ID, --id ID        id of indicator to update - find id by searching
                        indicator - query -v <indvalue>

```
