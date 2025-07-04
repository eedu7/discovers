import React from "react";
import Link from "next/link";

import { CardFooter } from "@/components/ui/card";

// TODO: Add proper links
export const LoginRegisterCardFooter = () => {
    return (
        <CardFooter>
            <p className="text-center text-sm">
                By continuing, you agree to Discover's&nbsp;
                <Link
                    className="cursor-pointer font-semibold underline hover:text-accent-foreground"
                    href="#"
                    prefetch={false}
                >
                    Terms of Service
                </Link>
                &nbsp;and
                <Link
                    className="cursor-pointer font-semibold underline hover:text-accent-foreground"
                    href="#"
                    prefetch={false}
                >
                    &nbsp;Privacy Notice
                </Link>
                .
            </p>
        </CardFooter>
    );
};
