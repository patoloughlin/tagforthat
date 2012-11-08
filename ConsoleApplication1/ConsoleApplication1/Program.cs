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
			Console.WriteLine("DA FUCK!");
			List<Responce> responces = new List<Responce>();
            int i = 1;
            bool keepRunning = true;
            while (keepRunning)
            {
                string url = "http://api.stackoverflow.com/1.1/questions?body=true&pagesize=100&tagged=c%23&page=" + i.ToString();

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
                            if (responceObject.page > 10)
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
            if(responces.Count > 0){
                SaveFile saveData = new SaveFile();
                saveData.questions = new List<Question>();
                saveData.count = responces[0].total;
                saveData.tag = "c#";
                foreach (var responce in responces)
                {
                    foreach (var question in responce.questions)
                    {
                        saveData.questions.Add(question);
                    }
                }
                using (System.IO.StreamWriter file = new System.IO.StreamWriter("csharp.json"))
                {
                    string output = JsonConvert.SerializeObject(saveData);
                    file.WriteLine(output);
                }
            }
			Console.WriteLine("Finished this shit!");
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