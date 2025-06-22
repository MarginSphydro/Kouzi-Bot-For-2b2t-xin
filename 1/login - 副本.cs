//MCCScript 1.0
MCC.LoadBot(new CombinedBot());

//MCCScript Extensions
public class CombinedBot : ChatBot
{
    private string lastHandledSK = "";
    private bool stopAll = false;
    private static Random rnd = new Random();

    private string[] insults = new string[] {
        "Mometure操你妈的，能不能告诉我",
        "Mometure你为什么只能念三字经的",
        "Mometure你怎么翻来覆去辗转反侧就这几个虎头蛇尾的破烂词汇",
        "Mometure操你妈小伙子你自己大大咧咧一窍不通是不是呢"
    };

    public override void Initialize()
    {
        Thread.Sleep(2000);
        SendText("/register nimabi nimabi");
        Thread.Sleep(1000);
        SendText("/login nimabi");
        Thread.Sleep(500);
        PerformInternalCommand("changeslot 3");
        Thread.Sleep(500);
        PerformInternalCommand("useitem");
    }

    public override void GetText(string line)
    {
        string text = System.Text.RegularExpressions.Regex.Replace(line, "§.", "");
        if (!text.StartsWith("<mark_7601> ")) return;

        string body = text.Substring(12).Trim();

        if (body.Equals("stop", StringComparison.OrdinalIgnoreCase))
        {
            stopAll = true;
            SendText("已停止所有操作");
            return;
        }

        if (body.StartsWith("SK ", StringComparison.OrdinalIgnoreCase))
        {
            string msg = body.Substring(3).Trim();
            if (msg != "" && msg != lastHandledSK)
            {
                lastHandledSK = msg;
                SendText(msg + " [" + GenTag(4) + "]");
            }
            return;
        }

        if (body.StartsWith("att ", StringComparison.OrdinalIgnoreCase))
        {
            string tgt = body.Substring(4).Trim().Split(' ')[0];
            stopAll = false;
            new System.Threading.Thread(() =>
            {
                int count = 0;
                while (!stopAll)
                {
                    string insult = insults[rnd.Next(insults.Length)];
                    SendText(tgt + " " + insult + " [" + GenTag(4) + "]");
                    count++;
                    Thread.Sleep(count < 3 ? 1000 + rnd.Next(2000) : 3000);
                }
            }) { IsBackground = true }.Start();
            return;
        }

        if (body.StartsWith("attsimp ", StringComparison.OrdinalIgnoreCase))
        {
            string msg = body.Substring(8).Trim();
            if (msg != "")
            {
                stopAll = false;
                new System.Threading.Thread(() =>
                {
                    int count = 0;
                    while (!stopAll)
                    {
                        SendText(msg + " [" + GenTag(4) + "]");
                        count++;
                        Thread.Sleep(count < 3 ? 1000 + rnd.Next(2000) : 3000);
                    }
                }) { IsBackground = true }.Start();
            }
            return;
        }

        if (body.StartsWith("attmsg ", StringComparison.OrdinalIgnoreCase))
        {
            string tgt = body.Substring(7).Trim().Split(' ')[0];
            stopAll = false;
            new System.Threading.Thread(() =>
            {
                while (!stopAll)
                {
                    string insult = insults[rnd.Next(insults.Length)];
                    SendText("/tell " + tgt + " " + insult + " [" + GenTag(4) + "]");
                    Thread.Sleep(1100);
                }
            }) { IsBackground = true }.Start();
            return;
        }

        if (body.StartsWith("attmsgsimp ", StringComparison.OrdinalIgnoreCase))
        {
            string[] parts = body.Split(new char[] { ' ' }, 3);
            if (parts.Length >= 3)
            {
                string tgt = parts[1];
                string msg = parts[2];
                stopAll = false;
                new System.Threading.Thread(() =>
                {
                    while (!stopAll)
                    {
                        SendText("/tell " + tgt + " " + msg + " [" + GenTag(4) + "]");
                        Thread.Sleep(1100);
                    }
                }) { IsBackground = true }.Start();
            }
            return;
        }
    }

    private string GenTag(int len)
    {
        string s = "";
        string chs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        for (int i = 0; i < len; i++)
            s += chs[rnd.Next(chs.Length)];
        return s;
    }
}
