import requests
import json
import hashlib
import ast

file = open('hash_codes.txt','r')
hash_secret = file.read()
file.close()

code = '''
public class CodinBlog{
	public static void main(String[] arg){
		System.out.println("Hello there");
	}
}
'''

code2 = '''
public class CodinBlog{
	public static void main(String[] arg){
		System.out.println("Hello there");
		int a = 1;
		while(true){
			a += 1;
		}

	}
}
'''

payload = {}
payload['user'] = '1'
payload['code'] = code2
payload['auth'] = hashlib.sha512(hash_secret+payload['user']).hexdigest()



url = 'http://104.236.77.41/run'
url2 = 'http://0.0.0.0:5000/'


res = requests.post(url, data=payload)
data = ast.literal_eval(res.text)
data['status_code'] = res.status_code
print data
# data = json.loads(res.text)
# data
# print res.status_code
# print data['result']
# print data['exit_code']





