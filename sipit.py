from pysip import Client
import argparse
from configparser import ConfigParser
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



if __name__ == "__main__":
   # remove proxy if it's set
   if 'http_proxy' in os.environ:
      del os.environ['http_proxy']
   if 'https_proxy' in os.environ:
      del os.environ['https_proxy']
   # load configuration
   config = ConfigParser()
   config.read(os.path.expanduser("~")+'/.sipit.ini')

   sip_client = Client(config['sip']['end_point'],config['sip']['api_key'],verify=False)
   parser = argparse.ArgumentParser(description="Add Indicators and query SIP")
   subparsers = parser.add_subparsers(dest='command')
   commands = [ 'create', 'query' ]

   query_parser = subparsers.add_parser('query',help="query aspects of SIP. query -h for more")
   query_parser.add_argument('-t','--types',default=False,action='store_true',help='list indicator types')
   query_parser.add_argument('-s','--sources',default=False,action='store_true',help='list sources')

   create_parser = subparsers.add_parser('create',help="add indicator to SIP. create -h for more",
           epilog="python3 sipit.py create -t 'String - PE' -r 'http://mycoollink' --tags 'malz,phish,stuff' -v 'something.pdb'")
   create_parser.add_argument('-s','--status',default='New',dest='status',
      help="Status of the indicator to add - New, Analyzed, Informational, Deprecated")
   create_parser.add_argument('-t','--indicator-type',required=True,dest='type',
      help="indicator type (URI - Path, String - PE, etc)")
   create_parser.add_argument('--campaign',dest='campaign',
      help="Campaign (APT32 or Oilrig)")
   create_parser.add_argument('--confidence',default='unknown',dest='confidence',
      help="Indicator Confidence Level")
   create_parser.add_argument('--impact',default='unknown',dest='impact',
      help="Indicator Impact")
   create_parser.add_argument('-v','--value',required=True,dest='value',
      help="Indicator Value")
   create_parser.add_argument('-r','--reference',required=True,dest='reference',
      help="Reference from where the indicator came from - context reference")
   create_parser.add_argument('--tags',dest='tags',
      help="comma delimited tags")
   create_parser.add_argument('--source',default="OSINT",dest='source',
      help="source of the info - OSINT, DSIE, RCISC, etc")

   args = parser.parse_args()

   if args.command is None:
      print("\n\n*****")
      print("You must specify one of the following commands:\n")
      print(cbinterface_commands)
      print("\n*****\n\n")
      parser.parse_args(['-h'])

   if args.command == 'query':
      if args.types:
         results = sip_client.get('/api/indicators/type')   
         for x in results:
            print(x['value'])
      if args.sources:
         results = sip_client.get('/api/intel/source')
         for x in results:
            print(x['value'])
 

   if args.command == 'create':
      user = config['sip']['user']

      data = { 'type' : args.type,
            'status' : args.status,
            'confidence' : args.confidence,
            'impact' : args.impact,
            'value' : args.value,
            'references' : [ {'source':args.source,'reference':args.reference}],
            'username' : user,
            'case_sensitive':False
      }
      if args.tags:
         data['tags'] = args.tags.split(',')
      if args.campaign:
         data['campaigns'] = [ args.campaign ]
   
      print(data)
      print(sip_client.post('/api/indicators',data))
