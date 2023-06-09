﻿// ITarget target = new Adapter();
// target.Request();
//
// /// <summary>
// /// This is the interface which the client expects.
// /// </summary>
// public interface ITarget
// {
//     void Request();
// }
//
// /// <summary>
// /// The adapter class adopts the interface which doesn't match the client's needs,
// /// and adapts it to the client's needs.
// /// </summary>
// public class Adapter : ITarget
// {
//     private readonly IAdaptee _adaptee = new Adaptee();
//     public void Request()
//     {
//         Console.WriteLine("Doing some extra work here, to fit the client's needs.");
//         Console.WriteLine("This work will be done on top of what the Adaptee does.");
//         
//         // Possibly do some other work
//         _adaptee.SpecificRequest();
//     }
// }
//
// /// <summary>
// /// The class / interface which doesn't fit the client's needs.
// /// </summary>
// public interface IAdaptee
// {
//     void SpecificRequest();
// }
// public class Adaptee : IAdaptee
// {
//     public void SpecificRequest()
//     {
//         Console.WriteLine("Called SpecificRequest()");
//     }
// }

var x = new A();
var y = new B();

Console.WriteLine("Made");
Console.WriteLine(B.x);
class A
{
    static A()
    {
        Console.WriteLine("A static");
    }

    public A()
    {
        Console.WriteLine("A inst");
    }
}

class B
{
    public static int x = Foo();

    static int Foo()
    {
        Console.WriteLine("B static");
        return 35;
    }

    public B()
    {
        Console.WriteLine("B inst");
    }
}