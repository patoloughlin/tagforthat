using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Test
{
    class Question
    {
        public List<string> tags { get; set; }
        public int answer_count {get; set;}
        public int favorite_count { get; set; }
        public int up_vote_count { get; set; }
        public int down_vote_count { get; set; }
        public int view_count { get; set; }
        public int score { get; set; }
        public int question_id {get; set;}
        public string title {get; set;}
        public string body {get; set;}
    }
}
