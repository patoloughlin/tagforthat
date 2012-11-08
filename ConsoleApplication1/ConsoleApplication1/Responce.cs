using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Test
{
    class Responce
    {
        public int total { get; set; }
        public int page { get; set; }
        public int pagesize { get; set; }
        public List<Question> questions { get; set; }
    }
}
