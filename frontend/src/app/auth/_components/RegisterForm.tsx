"use client";

import React from "react";
import Link from "next/link";

import { zodResolver } from "@hookform/resolvers/zod";
import { Loader2Icon } from "lucide-react";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { registerFormSchema } from "@/app/auth/schemas";

import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { PasswordInput } from "@/app/auth/_components/PasswordInput";

export const RegisterForm = () => {
    const form = useForm<z.infer<typeof registerFormSchema>>({
        resolver: zodResolver(registerFormSchema),
        defaultValues: {
            username: "",
            email: "",
            password: "",
        },
        mode: "all",
    });

    async function onSubmit(values: z.infer<typeof registerFormSchema>) {
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
                    name="username"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>
                                <span>
                                    Username<sup className="text-sm text-rose-800">*</sup>
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
                                    tabIndex={2}
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

                <Button
                    type="submit"
                    className="w-full font-semibold"
                    tabIndex={4}
                    disabled={form.formState.isSubmitting || !form.formState.isValid}
                >
                    {form.formState.isSubmitting ? (
                        <Loader2Icon className="repeat-infinite animate-spin" />
                    ) : (
                        "Register"
                    )}
                </Button>
                <p className="text-center text-xs md:text-sm">
                    Already have an account?&nbsp;
                    <Link
                        href="/auth/login"
                        className="cursor-pointer font-semibold underline hover:text-accent-foreground"
                        prefetch={false}
                    >
                        Log in
                    </Link>
                </p>
            </form>
        </Form>
    );
};
