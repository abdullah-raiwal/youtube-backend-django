import re


def extract_public_id(url):

  pattern = r"/upload/v\d+/(.*)"
  match = re.search(pattern, url)
  if match:
    return match.group(1)
  else:
    return None


