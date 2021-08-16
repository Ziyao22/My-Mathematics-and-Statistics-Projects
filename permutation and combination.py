int orders = 0;
String[] books = {"calculus","physics", "chemistry", "history", "literature",
"french", "astronomy"};
for(String a : books)
{
for(String b : books)
{
if(a.compareTo(b) < 0)
{
for(String c : books)
{
if(a.compareTo(c) < 0 && b.compareTo(c) < 0)
{
for(String d : books)
{
if(a.compareTo(d) < 0 &&
b.compareTo(d) < 0 &&
c.compareTo(d) < 0)
{
System.out.println(a + " " +
b + " " + c + " " +
d);
orders++;
}
}
}
}
}
}
}
System.out.println("Final count of all the possibilities: " + orders);
