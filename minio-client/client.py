from minio import  Minio
import os
import re
class client(object):

    def __init__(self,ak,sk,minioServer):
        self.ak = ak
        self.sk = sk
        self.address = minioServer
        self.obj = self.create_object()
        self.p = []
        self.bucket = ""
    def create_object(self):

        obj = Minio(endpoint=self.address,access_key=self.ak,secret_key=self.sk)
        return obj

    def put(self):
        pass

    def get(self):
        pass

    def cd(self,User_Selector_Prefix):
        print('执行cd',User_Selector_Prefix)
        if User_Selector_Prefix == '..':
            self.p.pop()
        else:
            self.p.append(User_Selector_Prefix)
        if len(self.p) == 1:
            self.select(Bucket=self.bucket)
        else:
            pattern = re.compile(r'(\w)+/(.*)')
            User_Selector_Prefix = pattern.match(os.path.sep.join(self.p)).group(2)
            self.select(Bucket=self.bucket,prefix=User_Selector_Prefix)
    def get_bucket(self):
        bucket_li = [i.name for i in self.obj.list_buckets()]
        return bucket_li

    def select(self,Bucket,prefix=""):
        select_file = []
        if prefix is None:
            list_obj = self.obj.list_objects(bucket_name=Bucket)
        else:
            list_obj = self.obj.list_objects(bucket_name=Bucket,prefix=prefix)
        for bucket_file in list_obj:
            print(bucket_file.object_name)
            select_file.append(bucket_file)

        if len(select_file) == 0:
            print("当前%s为空"%Bucket+prefix)
    def Base_Terminal(self):
        while True:

            print("一级菜单")
            print("当前bucket:%s"%self.get_bucket())
            User_Selector_Bucket = input("输入要查询的bucket名称:").strip()
            self.bucket = User_Selector_Bucket
            self.p.append(User_Selector_Bucket)
            if User_Selector_Bucket.lower() == "exit":
                break
            self.select(Bucket=User_Selector_Bucket)
            while True:
                path = os.path.sep.join(self.p)
                print("二级菜单")
                Action,User_Selector_Prefix = input("路径@{}:".format(path)).strip().split()
                if Action.lower() == "exit":
                    break
                if hasattr(self,Action):
                   resp = getattr(self,Action)
                   resp(User_Selector_Prefix)

                # p.append(User_Selector_Prefix)
                # pattern = re.compile(r'(\w)+/(.*)')
                # User_Selector_Prefix = pattern.match(os.path.sep.join(p)).group(2)
                # self.select(Bucket=User_Selector_Bucket,prefix=User_Selector_Prefix)






    def __call__(self, *args, **kwargs):
        self.Base_Terminal()
        # self.obj.make_bucket(bucket_name="yin")
        # path = "test/a"
        dummy_data = b''
        # self.obj.put_object(
        #     "yin",
        #     "test" + "user.txt",
        #     io.BytesIO(dummy_data),
        #     len(dummy_data),
        #     content_type = "application/octet-stream"
        # )
        # result = self.obj.fput_object(
        #     bucket_name="yin",
        #     object_name="data/" + 'user.txt',
        #     file_path="/Users/yintiecheng/PycharmProjects/pythonProject/课程/函数篇/user.txt")
        #
        # print(result.object_name,result.etag,result.version_id)
if __name__ == '__main__':

    obj = client(
        minioServer="play.min.io",
        ak="Q3AM3UQ867SPQQA43P2F",
        sk="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    print(obj())