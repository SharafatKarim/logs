+++
title = "Getting-started-with-csharp"
description = "- [Dotnet CLI](#dotnet-cli)
- [`Main` method and Top-level statement](#main-method-and-top-level-statement)"
+++

# Getting started with C#

- [Dotnet CLI](#dotnet-cli)
- [`Main` method and Top-level statement](#main-method-and-top-level-statement)
- [Namespace](#namespace)
- [Class](#class)
- [Record](#record)
- [Struct](#struct)
- [Enum](#enum)
- [Interface](#interface)
- [Anonymous Type](#anonymous-type)
- [Extension method](#extension-method)
- [Type inference with `var` keyword](#type-inference-with-var-keyword)
- [Object initializer](#object-initializer)
- [Generics](#generics)
- [Type casting](#type-casting)
- [Important Interfaces](#important-interfaces)
- [Lambda](#lambda)
- [Linq](#linq)
- [Asynchronous programming](#asynchronous-programming)

### Dotnet CLI

```bash
# create new solution
dotnet new sln --output <output_location> --name <solution_name>

# types of project
dotnet new list

# create a project
dotnet new <type> --output <output_location> --name <project_name>

# add project to solution
dotnet solution add <project_path>.csproj

# add a nuget pkg
dotnet add package Dumpify
```

### `Main` method and Top-level statement

```cs
class Program
{
   public static void Main(string[] args)
    {
        // Display the number of command line arguments.
        Console.WriteLine(args.Length);
    }
}
```

- The Main method is the entry point of an executable C# program; it is where the program control starts and ends.

- Starting in C# 9, you don't have to explicitly include a Main method in a console application project. Instead, you can use the top-level statements feature to minimize the code you have to write. In this case, the compiler generates a class and Main method entry point for the application.
- An application must have only one entry point. A project can have only one file with top-level statements.
- A file with top-level statements can also contain namespaces and type definitions, but they must come after the top-level statements.

### Namespace

- The namespace keyword is used to declare a scope that contains a set of related objects.
- The name of the `namespace` must be a valid C# identifier name.
- The compiler adds a default namespace. This unnamed namespace, sometimes referred to as the global namespace, is present in every file. It contains declarations not included in a declared namespace. Any identifier in the global namespace is available for use in a named namespace.
- File scoped namespace declarations enable you to declare that all types in a file are in a single namespace. File scoped namespaces can't include additional namespace declarations. You cannot declare a nested namespace or a second file-scoped namespace.

```cs
// file scoped namespace
namespace FileScoped;
class BlaBla {}

// block scoped namespace
namespace BlockScoped
{
 class BlaBla {}
}
```

### Class

- `readonly` means it can only be set either from constructor or by initialization.
- `const` means it can only be set by initialization.
- `static` members has to be accessed by class name.

```cs
public class User
{
    // const field
    public const string Country = "BD";

    // static readonly field
    public static readonly string Star = "Sun";

    // readonly field
    public readonly string Planet = "Earth";

    // field
    private bool _isEmailConfirmed;

    // field initializer
    public required string FullName { get; set; } = string.Empty;

    // auto property
    public required string UserName { get; set; }
    public string? Email { get; set; }

    // property with backing field
    public bool IsEmailConfirmed
    {
        get => _isEmailConfirmed;
        set
        {
            if (value && Email is not null) _isEmailConfirmed = value;
            else if (value is false && Email is null) _isEmailConfirmed = value;
        }
    }
}
```

### Record

```cs
public record AppUserLoginRequest(string UserName, string Password);
```

### Struct

- `struct` is value type, that means memory is allocated in stack rather than heap.
- A `struct` type can't inherit from other class or structure type and it can't be the base of a class. However, a structure type can implement interfaces.

```cs
public struct Person
{
    public required string FullName { get; set; }
    public int Age { get; set; }
}
```

`struct` type declarations with field initializers must include an explicitly declared constructor.

```cs
public struct Person
{
    public Person()
    {
    }

    public required string FullName { get; set; } = string.Empty;
    public int Age { get; set; } = 13;
}
```

### Enum

```cs
public enum BlogStatus : byte
{
    Published = 1,
    Draft
}
```

### Interface

- An interface defines a contract between user-defined types.
- By convention, an interface name starts with the letter I.
- All the members of an interface are public by default.
- An interface contains members including methods, properties, indexers, and events.
- A user-defined type that implements an interface must provide implementations for the members of the interface.
- A user-defined type can implement multiple interfaces.
- An interface can extend one or more interfaces.

```cs
interface IMyInterface
{
    void MyMethod();
}
```

### Anonymous Type

- Anonymous types allow you to encapsulate a set of read-only properties into a single object without having to define a class first.

- Behind the scenes, the compiler will generate the type name for the anonymous type.

```cs
var products = new[]
{
    new { Name = "Phone X", Price = 999.99 },
    new { Name = "Computer Y", Price = 1999.99 },
    new { Name = "Tablet Z", Price = 2999.99 }
};
```

### Extension method

```cs
using System.Linq;

namespace LearningCSharp;

public static class StringExtensions
{
    public static bool IsConstantCase(this string text)
    {
        return text.All(c => char.IsUpper(c));
    }
}
```

### Type inference with `var` keyword

- Use the `var` keyword for a variable with initialization from which the compiler can infer a type.
- The motto is: type should be only visible in one side of variable declaration, either right or left. `var` is used when type is evident in the left side.

```cs
using System;
using System.Collections.Generic;

IList<int> digitsList = [10, 20, 30, 35, 55, 66];
var digitsListWithVar = new List<int> { 10, 20, 30, 35, 55, 66 };

```

### Object initializer

```cs
var user = new User
{
    FullName = "John Doe",
    UserName = "john-doe"
};

User user = new()
{
    FullName = "John Doe",
    UserName = "john-doe"
};
```

### Generics

- Generics allow you to write code that works with more than one type.
- Generic constraints specify constraints on the type used as arguments for type parameters in generic type. Use the `where` keyword to specify generic constraints.

```cs
public static TNumber AddTwoNumbers<TNumber>(TNumber a, TNumber b)
    where TNumber : INumber<TNumber>
{
    return a + b;
}
```

### Type casting

- An object reference can be implicitly upcast to a base class reference. An upcast always succeeds.
- An object reference can also be explicitly downcast to a subclass reference. A downcast succeeds only if the object is compatible typed. Syntax: `(T)E`
- Use the `as` operator to perform a downcast that evaluates to null rather than throwing an exception.

```cs
var employee = new Employee
{
    Name = "John Doe",
    JobTitle = "C# Developer"
};

Person person = employee; // upcast
Employee employee2 = (Employee)person; // downcast
Employee? employee3 = person as Employee; // downcast


class Person
{
    public required string Name { get; set; }
}

class Employee : Person
{
    public required string JobTitle { get; set; }
}
```

### Important Interfaces

`IEnumerable<T>`: When we need a read-only operation, we can use `IEnumerable<T>`. It is for looping through the collection in the forward direction only. It supports deferred execution and filtering.

`ICollection<T>`: `ICollection<T>` extends `IEnumerable<T>`. ICollection allows to add or remove elements in the collection which is not possible with IEnumerable. But we still can’t perform any index-related operations. But we still can’t perform any index-related operations.

`IList<T>`: `IList<T>` extends `ICollection<T>`. It allows index-related operations like `Insert()`, `RemoveAt()` etc.

`IQueryable<T>`: Use for working with Database, processing will be done in the DB side. Fetched data can be translated to ICollection or IList easily.

```cs
using System;
using System.Collections.Generic;

IEnumerable<int> digitsEnumerable = [10, 20, 30, 35, 55, 66];
ICollection<int> digitsCollection = [10, 20, 30, 35, 55, 66];
IList<int> digitsList = [10, 20, 30, 35, 55, 66];
```

### Lambda

- A lambda expression can reference any variables including local variables, parameters, and members that are accessible from the location where you define the lambda expression.
- The variables referenced by a lambda expression are known as captured variables. When a lambda expression has captured variables, it is called a closure.
- When a lambda expression captures variables, the C# compiler needs to create a private class and instantiate it to store a reference to the captured variables. This incurs a small performance. you can use a static keyword to ensure that the lambda expression doesn’t capture any variables.

```cs
// expression lambda
var sum1 = (int a, int b) => a + b;

// statement lambda
var sum2 = (int a, int b) =>
{
    var sum = a + b;
    return sum;
};

// avoid capturing outer variable
int factor = 2;
var square = static (int x) => x * factor; // ERROR

```

### Linq

```cs
using System;
using System.Collections.Generic;
using System.Linq;

// 1. Data source
IList<int> digitsEnumerable = [10, 20, 30, 35, 55, 66];

// 2. Query creation
var numberQuerySyntax =
    from number in digitsEnumerable
    where number % 2 == 0
    select number;

var numberMethodSyntax = digitsEnumerable.Where(x => x % 2 == 0);

// 3. Query execution
foreach (var number in numberQuerySyntax)
{
    Console.WriteLine(number);
}

Console.WriteLine("############");

foreach (var number in numberMethodSyntax)
{
    Console.WriteLine(number);
}
```

### Asynchronous programming

```cs
    public class Todo
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public string? Title { get; set; }
        public bool Completed { get; set; }
    }

    public async Task<IList<Todo>> LoadTodoData()
    {
        using var httpClient = new HttpClient();
        var response = await httpClient.GetAsync("https://jsonplaceholder.typicode.com/todos");
        var todos = await response.Content.ReadFromJsonAsync<List<Todo>>();
        return todos ?? [];
    }
```

