import perplexity

def perp(request):
    try:
        request_json = request.get_json()

        perplexity_headers = request_json.get('perplexity_headers')
        perplexity_cookies = request_json.get('perplexity_cookies')
        emailnator_headers = request_json.get('emailnator_headers')
        emailnator_cookies = request_json.get('emailnator_cookies')
        query = request_json.get('query')
        mode = request_json.get('mode')
        focus = request_json.get('focus')

        perplexity_headers = repr(perplexity_headers).replace("'", '"')
        perplexity_cookies = repr(perplexity_cookies).replace("'", '"')
        emailnator_headers = repr(emailnator_headers).replace("'", '"')
        emailnator_cookies = repr(emailnator_cookies).replace("'", '"')

        print("Verbose")
        print(f"perplexity_headers: {perplexity_headers}")
        print(f"perplexity_cookies: {perplexity_cookies}")
        print(f"emailnator_headers: {emailnator_headers}")
        print(f"emailnator_cookies: {emailnator_cookies}")
        print(f"query: {query}")
        print(f"mode: {mode}")
        print(f"focus: {focus}")

        if perplexity_headers is None or perplexity_cookies is None or emailnator_headers is None or emailnator_cookies:
            return "We're missing the required cookies and headers", 400

        perplexity_cli, b = perplexity.Client(perplexity_headers, perplexity_cookies)
        perplexity_cli.create_account(emailnator_headers, emailnator_cookies)

        resp = perplexity_cli.search(query, mode='copilot', focus='internet', solvers={})
        return resp, 200

    except Exception as e:
        return str(e), 400
