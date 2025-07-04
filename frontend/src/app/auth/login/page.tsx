"use client";

import React from "react";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import Link from "next/link";
import { Separator } from "@/components/ui/separator";
import { PasswordInput } from "@/components/PasswordInput";

const formSchema = z.object({
    email: z.string().email(),
    password: z.string(),
});

function LoginPage() {
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            email: "",
            password: "",
        },
        mode: "all",
    });

    function onSubmit(values: z.infer<typeof formSchema>) {
        console.log(values);
    }

    return (
        <div className="grid place-content-center">
            <Card className="w-full min-w-[300px] md:w-md">
                <CardHeader>
                    <CardTitle>Log In</CardTitle>
                </CardHeader>
                <CardContent>
                    <Form {...form}>
                        <form
                            onSubmit={form.handleSubmit(onSubmit)}
                            className="space-y-4"
                        >
                            <FormField
                                control={form.control}
                                name="email"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>
                                            <span>
                                                Email<sup className="text-sm text-rose-800">*</sup>
                                            </span>
                                        </FormLabel>
                                        <FormControl>
                                            <Input
                                                placeholder=""
                                                {...field}
                                                tabIndex={1}
                                            />
                                        </FormControl>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="password"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>
                                            {" "}
                                            <span>
                                                Password<sup className="text-sm text-rose-800">*</sup>
                                            </span>
                                        </FormLabel>
                                        <FormControl>
                                            <PasswordInput
                                                {...field}
                                                tabIndex={3}
                                            />
                                        </FormControl>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                            <p className="text-right">
                                <Link
                                    href="/auth/forgot-password"
                                    className="w-full text-right text-sm font-semibold"
                                    prefetch={false}
                                >
                                    Forgot Password?
                                </Link>
                            </p>
                            <Button
                                type="submit"
                                className="w-full font-semibold"
                                tabIndex={3}
                                disabled={form.formState.isSubmitting || !form.formState.isValid}
                            >
                                Log in
                            </Button>
                            <p className="text-center text-sm">
                                Don't have an account?&nbsp;
                                <Link
                                    href="/auth/register"
                                    className="cursor-pointer font-semibold underline"
                                >
                                    Register for free.
                                </Link>
                            </p>
                        </form>
                    </Form>
                </CardContent>
                <Separator />
                <CardFooter>
                    <p className="text-center text-sm">
                        By continuing, you agree to Discover's&nbsp;
                        <Link
                            className="cursor-pointer font-semibold underline"
                            href="#"
                            prefetch={false}
                        >
                            Terms of Service
                        </Link>
                        &nbsp;and
                        <Link
                            className="cursor-pointer font-semibold underline"
                            href="#"
                            prefetch={false}
                        >
                            &nbsp;Privacy Notice
                        </Link>
                        .
                    </p>
                </CardFooter>
            </Card>
        </div>
    );
}

export default LoginPage;
