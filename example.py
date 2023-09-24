import perplexity

perplexity_headers = {
    'authority': 'www.perplexity.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8,nl;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=yET6Euw_uR_AQ-9azvclT,sentry-public_key=bb45aa7ca2dc43b6a7b6518e7c91e13d,sentry-trace_id=0a92976d4158464faf73d3add679e0c7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'next-auth.csrf-token=357285af423a69c7b499850ccb3b6262be77f174401f602818b5a6349d220e94%7C83f136d75962a6ded10673d474721959c5ff1f35fbec370161758588ef3ba3e3; trackingAllowed=true; _ga=GA1.1.1693210658.1694548309; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.perplexity.ai%2Fapi%2Fauth%2Fsignin-callback%3Fredirect%3Dhttps%253A%252F%252Fwww.perplexity.ai%252F; cf_clearance=496wDtV61oare.78b80XbPTthwFEQHFfM827qSYsbu4-1695149355-0-1-c37e973a.779b18e.947fc8da-160.0.0; _ga_SH9PRBQG23=GS1.1.1695568418.10.0.1695568418.0.0.0; __cflb=02DiuDyvFMmK5p9jVbWbam6CcSLCt41hZxGng6qrMZ6gU; AWSALB=0aXzgK5fgpfobqYL+b8nCZ3QC9O4IQAv+sJgzIotxI16NUDEiHrYm+JlnH11E/GsfSW9xlKzbtxdDidh5Hc69R7rd+kSNHrLkLI+gmB/sBPsLZi7D1UrAngKiIYr; AWSALBCORS=0aXzgK5fgpfobqYL+b8nCZ3QC9O4IQAv+sJgzIotxI16NUDEiHrYm+JlnH11E/GsfSW9xlKzbtxdDidh5Hc69R7rd+kSNHrLkLI+gmB/sBPsLZi7D1UrAngKiIYr',
    'origin': 'https://www.perplexity.ai',
    'referer': 'https://www.perplexity.ai/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '0a92976d4158464faf73d3add679e0c7-a8db06b6f1922c51-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
perplexity_cookies = {
    'next-auth.csrf-token': '357285af423a69c7b499850ccb3b6262be77f174401f602818b5a6349d220e94%7C83f136d75962a6ded10673d474721959c5ff1f35fbec370161758588ef3ba3e3',
    'trackingAllowed': 'true',
    '_ga': 'GA1.1.1693210658.1694548309',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.perplexity.ai%2Fapi%2Fauth%2Fsignin-callback%3Fredirect%3Dhttps%253A%252F%252Fwww.perplexity.ai%252F',
    'cf_clearance': '496wDtV61oare.78b80XbPTthwFEQHFfM827qSYsbu4-1695149355-0-1-c37e973a.779b18e.947fc8da-160.0.0',
    '_ga_SH9PRBQG23': 'GS1.1.1695568418.10.0.1695568418.0.0.0',
    '__cflb': '02DiuDyvFMmK5p9jVbWbam6CcSLCt41hZxGng6qrMZ6gU',
    'AWSALB': '0aXzgK5fgpfobqYL+b8nCZ3QC9O4IQAv+sJgzIotxI16NUDEiHrYm+JlnH11E/GsfSW9xlKzbtxdDidh5Hc69R7rd+kSNHrLkLI+gmB/sBPsLZi7D1UrAngKiIYr',
    'AWSALBCORS': '0aXzgK5fgpfobqYL+b8nCZ3QC9O4IQAv+sJgzIotxI16NUDEiHrYm+JlnH11E/GsfSW9xlKzbtxdDidh5Hc69R7rd+kSNHrLkLI+gmB/sBPsLZi7D1UrAngKiIYr',
}

emailnator_headers = {
    'authority': 'www.emailnator.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8,nl;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1885474800.1694548085; _ga_6R52Y0NSMR=GS1.1.1695568506.6.0.1695568506.0.0.0; XSRF-TOKEN=eyJpdiI6Ik9odlEyTnZDVzNiaHpicFFYYU9HcGc9PSIsInZhbHVlIjoibFoxMkd3R3pVZnkvblRQWURYcEJ0bUp0SjkrUHErcnZkcjZ1VXBLOTRiZUtDVk1lNmtmNklCdzlnalQyaG91bG16cFpDSWZtdWU2R2o2MXhJQVRTQnJyZ3k5TkR0YWxUS0F6VTdBUVVtenlqZjQyZWJaSm9VL3FVbnVUaHBwTHgiLCJtYWMiOiI3MGM1NmIwZmFjMmUwMDVmNWU2NmJlMDNjY2NmMjkyYmM1NzM4MDZkYjQyMTZhZWNhNWNjYjM0ZmM1OWVhYTA2IiwidGFnIjoiIn0%3D; gmailnator_session=eyJpdiI6InA5YnN4K2ZNM1VmeWpCZEV3bFpKaUE9PSIsInZhbHVlIjoiRUw1a1dVTkx4eU00eFMwdEdPTUN0Umg2K28vUGZSNXBrT2pJaHJ0Vm84TzlCL0JEbG95a2RCVTBrU1lhb0Rwd2YwSmJjUm53UXp5c3pTcVdrbE1DZHVWMSt3YlNrK1BvS0VQQ081UjNaRXlDQ0NMbXFPS3cxWElia0JRMXZYa1oiLCJtYWMiOiIzZTY0ZTVmYWViNDExNzkzNDA5YTc4ODhkMTE1ZDk3OWIwZDhlZjg2ZTY4ODExZTY1MjY3ZmFhNzkxZTFhNTc2IiwidGFnIjoiIn0%3D',
    'origin': 'https://www.emailnator.com',
    'referer': 'https://www.emailnator.com/inbox/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6Ik9odlEyTnZDVzNiaHpicFFYYU9HcGc9PSIsInZhbHVlIjoibFoxMkd3R3pVZnkvblRQWURYcEJ0bUp0SjkrUHErcnZkcjZ1VXBLOTRiZUtDVk1lNmtmNklCdzlnalQyaG91bG16cFpDSWZtdWU2R2o2MXhJQVRTQnJyZ3k5TkR0YWxUS0F6VTdBUVVtenlqZjQyZWJaSm9VL3FVbnVUaHBwTHgiLCJtYWMiOiI3MGM1NmIwZmFjMmUwMDVmNWU2NmJlMDNjY2NmMjkyYmM1NzM4MDZkYjQyMTZhZWNhNWNjYjM0ZmM1OWVhYTA2IiwidGFnIjoiIn0=',
}
emailnator_cookies = {
    '_ga': 'GA1.1.1885474800.1694548085',
    '_ga_6R52Y0NSMR': 'GS1.1.1695568506.6.0.1695568506.0.0.0',
    'XSRF-TOKEN': 'eyJpdiI6Ik9odlEyTnZDVzNiaHpicFFYYU9HcGc9PSIsInZhbHVlIjoibFoxMkd3R3pVZnkvblRQWURYcEJ0bUp0SjkrUHErcnZkcjZ1VXBLOTRiZUtDVk1lNmtmNklCdzlnalQyaG91bG16cFpDSWZtdWU2R2o2MXhJQVRTQnJyZ3k5TkR0YWxUS0F6VTdBUVVtenlqZjQyZWJaSm9VL3FVbnVUaHBwTHgiLCJtYWMiOiI3MGM1NmIwZmFjMmUwMDVmNWU2NmJlMDNjY2NmMjkyYmM1NzM4MDZkYjQyMTZhZWNhNWNjYjM0ZmM1OWVhYTA2IiwidGFnIjoiIn0%3D',
    'gmailnator_session': 'eyJpdiI6InA5YnN4K2ZNM1VmeWpCZEV3bFpKaUE9PSIsInZhbHVlIjoiRUw1a1dVTkx4eU00eFMwdEdPTUN0Umg2K28vUGZSNXBrT2pJaHJ0Vm84TzlCL0JEbG95a2RCVTBrU1lhb0Rwd2YwSmJjUm53UXp5c3pTcVdrbE1DZHVWMSt3YlNrK1BvS0VQQ081UjNaRXlDQ0NMbXFPS3cxWElia0JRMXZYa1oiLCJtYWMiOiIzZTY0ZTVmYWViNDExNzkzNDA5YTc4ODhkMTE1ZDk3OWIwZDhlZjg2ZTY4ODExZTY1MjY3ZmFhNzkxZTFhNTc2IiwidGFnIjoiIn0%3D',
}


perplexity_cli = perplexity.Client(perplexity_headers, perplexity_cookies)
perplexity_cli.create_account(emailnator_headers, emailnator_cookies) # Creates a new gmail, so your 5 copilots will be renewed. You can pass this one if you are not going to use "copilot" mode


# takes a string as query, and returns a string as answer.
def my_text_prompt_solver(query):
    return input(f'{query}: ')

# takes a string as description and a dictionary as options. Dictionary consists of ids and values. Example: {1: "Orange", 2: "Banana"}
# returns a list of integers which are ids of selected options. Let's say you selected "Banana", function should return [2]
def my_checkbox_prompt_solver(description, options):
    print(description + '\n' + '\n'.join([str(x) + ' - ' + options[x] for x in options]))
    return [int(input('--> '))]


# modes = ['concise', 'copilot']
# focus = ['internet', 'scholar', 'writing', 'wolfram', 'youtube', 'reddit']
# files = file list, each element of list is tuple like this: (data, filetype) perplexity supports two file types, txt and pdf
# follow_up = last query info for follow-up queries, you can directly pass response json from a query, look at second example below.
# solvers, list of functions to answer questions of ai while using copilot, there are 2 type of solvers, text and checkbox. If you do not define function for a solver, questions in that solver type will be skipped
resp = perplexity_cli.search('What is the best programming language for web development', mode='concise', focus='internet', solvers={
    'text': my_text_prompt_solver,
    'checkbox': my_checkbox_prompt_solver
    })
print(resp)

# perplexity_cli.create_account(emailnator_headers, emailnator_cookies) # Call this function again when you're out of copilots