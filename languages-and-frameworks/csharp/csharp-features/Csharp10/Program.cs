﻿global using Csharp10;

Console.WriteLine("[C# 10]: Program starting");

// Constant Interpolated Strings
var constantInterpolatedStringExample = new ConstantInterpolatedStrings();
constantInterpolatedStringExample.DemonstrateBefore();
constantInterpolatedStringExample.DemonstrateAfter();


// Async Method Builders
await AsyncMethodBuilderDemo.Demonstrate();

Console.WriteLine("[C# 10]: Program ended");