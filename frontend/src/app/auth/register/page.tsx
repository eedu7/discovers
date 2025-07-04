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
import { PasswordInput } from "@/app/auth/_components/PasswordInput";
import { Loader2Icon } from "lucide-react";

const formSchema = z.object({
    username: z.string(),
    email: z.string().email(),
    password: z.string(),
});

function RegisterPage() {
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            username: "",
            email: "",
            password: "",
        },
        mode: "all",
    });

    async function onSubmit(values: z.infer<typeof formSchema>) {
        console.log(values);
    }

    return (
        <div className="grid place-content-center px-2 md:px-0">
            <Card className="w-full md:w-md">
                <CardHeader>
                    <CardTitle>Register</CardTitle>
                </CardHeader>
                <CardContent>
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
                                    className="cursor-pointer font-semibold underline"
                                    prefetch={false}
                                >
                                    Log in
                                </Link>
                            </p>
                        </form>
                    </Form>
                </CardContent>
                <Separator />
                <CardFooter>
                    <p className="text-center text-xs md:text-sm">
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

export default RegisterPage;
