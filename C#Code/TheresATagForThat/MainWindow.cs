using System;
using Gtk;
using Newtonsoft.Json;
using TheresATagForThat;
using System.Net.Sockets;
using System.Net;

public partial class MainWindow: Gtk.Window
{	
	public MainWindow (): base (Gtk.WindowType.Toplevel)
	{
		Build ();
	}
	
	protected void OnDeleteEvent (object sender, DeleteEventArgs a)
	{
		Application.Quit ();
		a.RetVal = true;
	}

	protected void OnClickButtonClicked (object sender, EventArgs e)
	{
		TestObject temp = new TestObject();
		temp.number = 1;
		temp.Name = this.entry1.Text;
		this.label1.Text = JsonConvert.SerializeObject(temp).ToString();
	}
}
