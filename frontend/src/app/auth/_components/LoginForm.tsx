"use client";

import React from "react";
import Link from "next/link";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { loginFormSchema } from "@/app/auth/schemas";

import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { PasswordInput } from "@/app/auth/_components/PasswordInput";

export const LoginForm = () => {
    const form = useForm<z.infer<typeof loginFormSchema>>({
        resolver: zodResolver(loginFormSchema),
        defaultValues: {
            email: "",
            password: "",
        },
        mode: "all",
    });

    function onSubmit(values: z.infer<typeof loginFormSchema>) {
        console.log(values);
    }

    return (
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
                        className="w-full text-right text-sm font-semibold hover:text-accent-foreground cursor-pointer hover:underline"
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
                        className="cursor-pointer font-semibold underline hover:text-accent-foreground"
                    >
                        Register
                    </Link>
                </p>
            </form>
        </Form>
    );
};
