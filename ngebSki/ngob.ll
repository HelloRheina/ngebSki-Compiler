; ModuleID = "/Users/ceciliaalexa/Desktop/ngebSki/CodeGen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"() 
{
entry:
  %"a" = alloca i32
  store i32 5, i32* %"a"
  %"b" = alloca i32
  store i32 10, i32* %"b"
  %"c" = alloca i32
  store i32 -15, i32* %"c"
  %"d" = alloca i32
  store i32 20, i32* %"d"
  %"e" = alloca i32
  store i32 25, i32* %"e"
  %"f" = alloca i32
  store i32 -30, i32* %"f"
  %"g" = alloca i32
  store i32 35, i32* %"g"
  %"h" = alloca i32
  store i32 -40, i32* %"h"
  %"i" = alloca i32
  store i32 45, i32* %"i"
  %"j" = alloca i32
  store i32 -50, i32* %"j"
  %"k" = alloca i32
  store i32 55, i32* %"k"
  %"l" = alloca i32
  store i32 -60, i32* %"l"
  %"m" = alloca i32
  store i32 65, i32* %"m"
  %"n" = alloca i32
  store i32 -70, i32* %"n"
  %"o" = alloca i32
  store i32 75, i32* %"o"
  %"result1" = alloca i32
  store i32 0, i32* %"result1"
  br label %"loop_cond"
loop_cond:
  %"a.load" = load i32, i32* %"a"
  %".19" = icmp ule i32 %"a.load", 50
  br i1 %".19", label %"loop_body", label %"loop_end"
loop_body:
  %"result1.load" = load i32, i32* %"result1"
  %"a.load.1" = load i32, i32* %"a"
  %"b.load" = load i32, i32* %"b"
  %"multmp" = mul i32 %"a.load.1", %"b.load"
  %"sumtmp" = add i32 %"result1.load", %"multmp"
  %"c.load" = load i32, i32* %"c"
  %"d.load" = load i32, i32* %"d"
  %"divtmp" = sdiv i32 %"c.load", %"d.load"
  %"subtmp" = sub i32 %"sumtmp", %"divtmp"
  %"e.load" = load i32, i32* %"e"
  %"sumtmp.1" = add i32 %"subtmp", %"e.load"
  store i32 %"sumtmp.1", i32* %"result1"
  %"a.load.2" = load i32, i32* %"a"
  %"sumtmp.2" = add i32 %"a.load.2", 5
  store i32 %"sumtmp.2", i32* %"a"
  br label %"loop_cond"
loop_end:
  %"result2" = alloca i32
  store i32 1, i32* %"result2"
  br label %"loop_cond.1"
loop_cond.1:
  %"b.load.1" = load i32, i32* %"b"
  %".26" = icmp uge i32 %"b.load.1", -50
  br i1 %".26", label %"loop_body.1", label %"loop_end.1"
loop_body.1:
  %"result2.load" = load i32, i32* %"result2"
  %"f.load" = load i32, i32* %"f"
  %"g.load" = load i32, i32* %"g"
  %"divtmp.1" = sdiv i32 %"f.load", %"g.load"
  %"h.load" = load i32, i32* %"h"
  %"sumtmp.3" = add i32 %"divtmp.1", %"h.load"
  %"i.load" = load i32, i32* %"i"
  %"j.load" = load i32, i32* %"j"
  %"multmp.1" = mul i32 %"i.load", %"j.load"
  %"subtmp.1" = sub i32 %"sumtmp.3", %"multmp.1"
  %"multmp.2" = mul i32 %"result2.load", %"subtmp.1"
  store i32 %"multmp.2", i32* %"result2"
  %"b.load.2" = load i32, i32* %"b"
  %"subtmp.2" = sub i32 %"b.load.2", 10
  store i32 %"subtmp.2", i32* %"b"
  br label %"loop_cond.1"
loop_end.1:
  %"result3" = alloca i32
  store i32 0, i32* %"result3"
  br label %"loop_cond.2"
loop_cond.2:
  %"c.load.1" = load i32, i32* %"c"
  %".33" = icmp ult i32 %"c.load.1", 0
  br i1 %".33", label %"loop_body.2", label %"loop_end.2"
loop_body.2:
  %"result3.load" = load i32, i32* %"result3"
  %"k.load" = load i32, i32* %"k"
  %"l.load" = load i32, i32* %"l"
  %"sumtmp.4" = add i32 %"k.load", %"l.load"
  %"m.load" = load i32, i32* %"m"
  %"divtmp.2" = sdiv i32 %"sumtmp.4", %"m.load"
  %"sumtmp.5" = add i32 %"result3.load", %"divtmp.2"
  %"n.load" = load i32, i32* %"n"
  %"o.load" = load i32, i32* %"o"
  %"multmp.3" = mul i32 %"n.load", %"o.load"
  %"subtmp.3" = sub i32 %"sumtmp.5", %"multmp.3"
  store i32 %"subtmp.3", i32* %"result3"
  %"c.load.2" = load i32, i32* %"c"
  %"sumtmp.6" = add i32 %"c.load.2", 5
  store i32 %"sumtmp.6", i32* %"c"
  br label %"loop_cond.2"
loop_end.2:
  %"result4" = alloca i32
  store i32 1000, i32* %"result4"
  br label %"loop_cond.3"
loop_cond.3:
  %"d.load.1" = load i32, i32* %"d"
  %".40" = icmp ugt i32 %"d.load.1", 0
  br i1 %".40", label %"loop_body.3", label %"loop_end.3"
loop_body.3:
  %"result4.load" = load i32, i32* %"result4"
  %"a.load.3" = load i32, i32* %"a"
  %"b.load.3" = load i32, i32* %"b"
  %"sumtmp.7" = add i32 %"a.load.3", %"b.load.3"
  %"c.load.3" = load i32, i32* %"c"
  %"d.load.2" = load i32, i32* %"d"
  %"subtmp.4" = sub i32 %"c.load.3", %"d.load.2"
  %"multmp.4" = mul i32 %"sumtmp.7", %"subtmp.4"
  %"e.load.1" = load i32, i32* %"e"
  %"divtmp.3" = sdiv i32 %"multmp.4", %"e.load.1"
  %"subtmp.5" = sub i32 %"result4.load", %"divtmp.3"
  %"f.load.1" = load i32, i32* %"f"
  %"sumtmp.8" = add i32 %"subtmp.5", %"f.load.1"
  store i32 %"sumtmp.8", i32* %"result4"
  %"d.load.3" = load i32, i32* %"d"
  %"subtmp.6" = sub i32 %"d.load.3", 10
  store i32 %"subtmp.6", i32* %"d"
  br label %"loop_cond.3"
loop_end.3:
  %"result5" = alloca i32
  store i32 0, i32* %"result5"
  br label %"loop_cond.4"
loop_cond.4:
  %"e.load.2" = load i32, i32* %"e"
  %".47" = icmp ult i32 %"e.load.2", 100
  br i1 %".47", label %"loop_body.4", label %"loop_end.4"
loop_body.4:
  %"result5.load" = load i32, i32* %"result5"
  %"g.load.1" = load i32, i32* %"g"
  %"h.load.1" = load i32, i32* %"h"
  %"divtmp.4" = sdiv i32 %"g.load.1", %"h.load.1"
  %"sumtmp.9" = add i32 %"result5.load", %"divtmp.4"
  %"i.load.1" = load i32, i32* %"i"
  %"j.load.1" = load i32, i32* %"j"
  %"multmp.5" = mul i32 %"i.load.1", %"j.load.1"
  %"subtmp.7" = sub i32 %"sumtmp.9", %"multmp.5"
  %"k.load.1" = load i32, i32* %"k"
  %"sumtmp.10" = add i32 %"subtmp.7", %"k.load.1"
  store i32 %"sumtmp.10", i32* %"result5"
  %"e.load.3" = load i32, i32* %"e"
  %"sumtmp.11" = add i32 %"e.load.3", 15
  store i32 %"sumtmp.11", i32* %"e"
  br label %"loop_cond.4"
loop_end.4:
  %"result6" = alloca i32
  store i32 0, i32* %"result6"
  br label %"loop_cond.5"
loop_cond.5:
  %"f.load.2" = load i32, i32* %"f"
  %".54" = icmp ult i32 %"f.load.2", -10
  br i1 %".54", label %"loop_body.5", label %"loop_end.5"
loop_body.5:
  %"result6.load" = load i32, i32* %"result6"
  %"l.load.1" = load i32, i32* %"l"
  %"m.load.1" = load i32, i32* %"m"
  %"subtmp.8" = sub i32 %"l.load.1", %"m.load.1"
  %"n.load.1" = load i32, i32* %"n"
  %"o.load.1" = load i32, i32* %"o"
  %"sumtmp.12" = add i32 %"n.load.1", %"o.load.1"
  %"divtmp.5" = sdiv i32 %"subtmp.8", %"sumtmp.12"
  %"a.load.4" = load i32, i32* %"a"
  %"multmp.6" = mul i32 %"divtmp.5", %"a.load.4"
  %"sumtmp.13" = add i32 %"result6.load", %"multmp.6"
  store i32 %"sumtmp.13", i32* %"result6"
  %"f.load.3" = load i32, i32* %"f"
  %"sumtmp.14" = add i32 %"f.load.3", 5
  store i32 %"sumtmp.14", i32* %"f"
  br label %"loop_cond.5"
loop_end.5:
  %".59" = bitcast [12 x i8]* @"fstr_0" to i8*
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".59", i8* %".59")
  %"result1.load.1" = load i32, i32* %"result1"
  %".61" = bitcast [4 x i8]* @"fstr_1" to i8*
  %".62" = call i32 (i8*, ...) @"printf"(i8* %".61", i32 %"result1.load.1")
  %".63" = bitcast [12 x i8]* @"fstr_2" to i8*
  %".64" = call i32 (i8*, ...) @"printf"(i8* %".63", i8* %".63")
  %"result2.load.1" = load i32, i32* %"result2"
  %".65" = bitcast [4 x i8]* @"fstr_3" to i8*
  %".66" = call i32 (i8*, ...) @"printf"(i8* %".65", i32 %"result2.load.1")
  %".67" = bitcast [12 x i8]* @"fstr_4" to i8*
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67", i8* %".67")
  %"result3.load.1" = load i32, i32* %"result3"
  %".69" = bitcast [4 x i8]* @"fstr_5" to i8*
  %".70" = call i32 (i8*, ...) @"printf"(i8* %".69", i32 %"result3.load.1")
  %".71" = bitcast [12 x i8]* @"fstr_6" to i8*
  %".72" = call i32 (i8*, ...) @"printf"(i8* %".71", i8* %".71")
  %"result4.load.1" = load i32, i32* %"result4"
  %".73" = bitcast [4 x i8]* @"fstr_7" to i8*
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73", i32 %"result4.load.1")
  %".75" = bitcast [12 x i8]* @"fstr_8" to i8*
  %".76" = call i32 (i8*, ...) @"printf"(i8* %".75", i8* %".75")
  %"result5.load.1" = load i32, i32* %"result5"
  %".77" = bitcast [4 x i8]* @"fstr_9" to i8*
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".77", i32 %"result5.load.1")
  %".79" = bitcast [12 x i8]* @"fstr_10" to i8*
  %".80" = call i32 (i8*, ...) @"printf"(i8* %".79", i8* %".79")
  %"result6.load.1" = load i32, i32* %"result6"
  %".81" = bitcast [4 x i8]* @"fstr_11" to i8*
  %".82" = call i32 (i8*, ...) @"printf"(i8* %".81", i32 %"result6.load.1")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr_0" = internal constant [12 x i8] c"result1 : \0a\00"
@"fstr_1" = internal constant [4 x i8] c"%i\0a\00"
@"fstr_2" = internal constant [12 x i8] c"result2 : \0a\00"
@"fstr_3" = internal constant [4 x i8] c"%i\0a\00"
@"fstr_4" = internal constant [12 x i8] c"result3 : \0a\00"
@"fstr_5" = internal constant [4 x i8] c"%i\0a\00"
@"fstr_6" = internal constant [12 x i8] c"result4 : \0a\00"
@"fstr_7" = internal constant [4 x i8] c"%i\0a\00"
@"fstr_8" = internal constant [12 x i8] c"result5 : \0a\00"
@"fstr_9" = internal constant [4 x i8] c"%i\0a\00"
@"fstr_10" = internal constant [12 x i8] c"result6 : \0a\00"
@"fstr_11" = internal constant [4 x i8] c"%i\0a\00"