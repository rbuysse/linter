#!/usr/bin/env python3
import yaml

def find_disable_comment(file_path):
    with open(file_path, 'r') as stream:
        loader = yaml.Loader(stream)
        while loader.check_token():
            token = loader.get_token()
            print(token)
            if isinstance(token, yaml.BlockMappingStartToken):
                next_token = loader.peek_token()
                # if isinstance(next_token, yaml.CommentToken) and 'disable' in next_token.value:
                #     return next_token.value

# Use the function
comment = find_disable_comment('test/externalsecrets.yaml')
print(comment)
