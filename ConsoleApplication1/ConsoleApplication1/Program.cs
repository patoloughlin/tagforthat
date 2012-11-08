using System;
using System.Collections.Generic;
using System.Text;
using System.Net;
using System.IO;
using System.IO.Compression;
using Newtonsoft.Json;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
			List<string> tags = new List<string>{"c#",
				"java",
				"php",
				"javascript",
				"android",
				"jquery",
				"c++",
				"iphone",
				"asp.net",
				"python",
				".net",
				"html",
				"mysql",
				"objective-c",
				"ios",
				"sql",
				"css",
				"ruby-on-rails",
				"c",
				"ruby",
				"sql-server",
				"wpf",
				"xml",
				"ajax",
				"regex",
				"asp.net-mvc",
				"database",
				"xcode",
				"django",
				"linux",
				"windows",
				"arrays",
				"vb.net",
				"facebook",
				"ruby-on-rails-3",
				"eclipse",
				"json",
				"winforms",
				"string",
				"multithreading",
				"asp.net-mvc-3",
				"visual-studio-2010",
				"wcf",
				"performance",
				"image",
				"osx",
				"algorithm",
				"linq",
				"web-services",
				"visual-studio"};
			for(int k = 0; k < tags.Count; k++){
				string tag = tags[k];
				Console.WriteLine("Starting to pull for tag: " + tag + ".");
				if(tag == "c#"){
					tag = "c%23";
				}
				//Full loop for current tag
				List<Responce> responces = new List<Responce>();
	            int i = 1;
	            bool keepRunning = true;
	            while (keepRunning)
	            {
	                string url = "http://api.stackoverflow.com/1.1/questions?body=true&pagesize=100&tagged=" + tag + "&page=" + i.ToString();

	                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
	                request.Timeout = 5000;

	                try
	                {
	                    using (WebResponse response = (HttpWebResponse)request.GetResponse())
	                    using (Stream csStream = new GZipStream(response.GetResponseStream(), CompressionMode.Decompress))
	                    {
	                        byte[] bytes = ReadFully(csStream);
	                        string responceString = Encoding.UTF8.GetString(bytes);
	                        try
	                        {
	                            Responce responceObject = JsonConvert.DeserializeObject<Responce>(responceString);
	                            responces.Add(responceObject);
	                            if (responceObject.total < responceObject.page * responceObject.pagesize || responceObject.page > 10)
	                            {
	                                keepRunning = false;
	                            }
	                        }
	                        catch{
	                        }
	                    }


	                }
	                catch (WebException)
	                {
	                    Console.WriteLine("Error Occured");
	                }
	                i++;
	            }
				if(tag == "c%23")
					tag = "c#";
	            if(responces.Count > 0){
	                SaveFile saveData = new SaveFile();
	                saveData.questions = new List<Question>();
	                saveData.count = responces[0].total;
	                saveData.tag = tag;
	                foreach (var responce in responces)
	                {
	                    foreach (var question in responce.questions)
	                    {
	                        saveData.questions.Add(question);
	                    }
	                }
	                using (System.IO.StreamWriter file = new System.IO.StreamWriter((tag + ".json")))
	                {
	                    string output = JsonConvert.SerializeObject(saveData);
	                    file.WriteLine(output);
	                }
	            }
				Console.WriteLine("Finishing pulling for tag: " + tag + ".");
			}
        }

        public static byte[] ReadFully(Stream input)
        {
            byte[] buffer = new byte[16 * 1024];
            using (MemoryStream ms = new MemoryStream())
            {
                int read;
                while ((read = input.Read(buffer, 0, buffer.Length)) > 0)
                {
                    ms.Write(buffer, 0, read);
                }
                return ms.ToArray();
            }
        }
    }
}