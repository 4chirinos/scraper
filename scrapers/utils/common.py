from urllib.parse import urlencode, parse_qs, urlsplit, urlunsplit

def set_query_string_parameter_from_url(url, name, value):
  scheme, netloc, path, query_string, fragment = urlsplit(url)
  query_string_params = parse_qs(query_string)
  query_string_params[name] = [value]
  new_query_string = urlencode(query_string_params, doseq = True)
  return urlunsplit((scheme, netloc, path, new_query_string, fragment))

def set_query_string_parameter_from_qs(query_string, name, value):
  query_string_params = dict()
  elements = list()
  parameters = query_string.split('&')
  for parameter in parameters:
    pair = parameter.split('=')
    query_string_params[pair[0]] = pair[1]
  query_string_params[name] = value
  for key, value in query_string_params.items():
    elements.append('{}={}'.format(key, value))
  return '&'.join(elements)